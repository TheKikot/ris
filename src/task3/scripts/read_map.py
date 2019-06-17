#!/usr/bin/python
from __future__ import print_function

#import random
#import sys
import rospy
import cv2
#import math
import numpy as np
import tf2_geometry_msgs
import tf2_ros
from matplotlib import pyplot as plt
from sensor_msgs.msg import Image
from geometry_msgs.msg import PointStamped, Vector3, Pose
from cv_bridge import CvBridge, CvBridgeError
from visualization_msgs.msg import Marker, MarkerArray
from std_msgs.msg import ColorRGBA
from task3.srv import *

global bridge, dictm, params

dictm = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_6X6_250)

# The object that we will pass to the markerDetect function
params =  cv2.aruco.DetectorParameters_create()


def read_map_from_img():
	# parameter za spodnjo mejo iskanja projekcije
	MIN_MATCH_COUNT = 10
	# parameter za velikost krizca v pikslih
	krizecSize = 20
	
	## preberi sliko ---------- 	
	
	'''
	# pridobivanje slike
	data = rospy.wait_for_message('/camera/rgb/image_raw', Image)
  print('slika prejeta')
  # pretvorba slike
  try:
		#print('converting image')
		global bridge
		img = bridge.imgmsg_to_cv2(data, 'bgr8')
		print('slika pretvorjena')
  except CvBridgeError, e:
    print(e)
  '''
	cv_image = cv2.imread('/home/kikot/ROS/map_pictures/map_blue.jpg', 0)
	# ce algoritem ne bo dovolj robusten, dodaj tu homografijo z markerji!
	print("berem sliko")
	
	#####################################################
	## markerji
	##################################################
	
	corners, ids, rejected_corners = cv2.aruco.detectMarkers(cv_image,dictm,parameters=params)
		        
	# Increase proportionally if you want a larger image
	image_size=(351,248,3)
	marker_side=50

	img_out = np.zeros(image_size, np.uint8)
	out_pts = np.array([[marker_side/2,img_out.shape[0]-marker_side/2],
		                  [img_out.shape[1]-marker_side/2,img_out.shape[0]-marker_side/2],
		                  [marker_side/2,marker_side/2],
		                  [img_out.shape[1]-marker_side/2,marker_side/2]])

	src_points = np.zeros((4,2))
	cens_mars = np.zeros((4,2))

	if not ids is None:
		if len(ids)==4:
			print('4 Markers detected')

			for idx in ids:
			  # Calculate the center point of all markers
			  cors = np.squeeze(corners[idx[0]-1])
			  cen_mar = np.mean(cors,axis=0)
			  cens_mars[idx[0]-1]=cen_mar
			  cen_point = np.mean(cens_mars,axis=0)

			for coords in cens_mars:
		    #  Map the correct source points
				if coords[0]<cen_point[0] and coords[1]<cen_point[1]:
					src_points[2]=coords
				elif coords[0]<cen_point[0] and coords[1]>cen_point[1]:
					src_points[0]=coords
				elif coords[0]>cen_point[0] and coords[1]<cen_point[1]:
					src_points[3]=coords
				else:
					src_points[1]=coords

			h, status = cv2.findHomography(src_points, out_pts)
			img_out = cv2.warpPerspective(cv_image, h, (img_out.shape[1],img_out.shape[0]))
			cv2.imwrite('/home/kikot/ROS/uncropped_image.jpg', img_out)			
			
			###################################################
			## racunanje homografije za zemljevid
			##################################################

			## SURF ----------
			img = img_out[115:265,55:205]
			#cv2.imwrite('/home/kikot/ROS/cropped_image.jpg', img)

			h,w = img.shape
			# ref_img = cv2.imread('/home/kikot/ROS/map_pictures/map_blue.jpg', 0)
			ref_img = cv2.imread('/home/kikot/ROS/maps/mapa_ref.pgm', 0)
			# za realno uporabo parameter spremenimo na vrednost med 300 in 500
			surf = cv2.xfeatures2d.SURF_create(400)
			# kp -> keypoints, des -> deskriptor slike
			kp, des = surf.detectAndCompute(img,None)
			ref_kp, ref_des = surf.detectAndCompute(ref_img,None)
			img_kp = cv2.drawKeypoints(img,kp,None,(255,0,0),4)
			ref_img_kp = cv2.drawKeypoints(ref_img,ref_kp,None,(255,0,0),4)
			#plt.imshow(img2),plt.show()
			#cv2.imwrite('/home/kikot/ROS/sift_keypoints.jpg', ref_img_kp)

			## poisci homografijo ----------

			FLANN_INDEX_KDTREE = 1
			index_params = dict(algorithm = FLANN_INDEX_KDTREE, trees = 5)
			search_params = dict(checks = 50)
			flann = cv2.FlannBasedMatcher(index_params, search_params)
			matches = flann.knnMatch(des, ref_des, k=2)
			# store all the good matches as per Lowe's ratio test.
			good = []
			for m,n in matches:
				if m.distance < 0.7*n.distance:
					good.append(m)
	
			# if enough matches are found, proceed with projection
			if len(good)>MIN_MATCH_COUNT:
				src_pts = np.float32([ kp[m.queryIdx].pt for m in good ]).reshape(-1,1,2)
				dst_pts = np.float32([ ref_kp[m.trainIdx].pt for m in good ]).reshape(-1,1,2)
				M, mask = cv2.findHomography(src_pts, dst_pts, cv2.RANSAC,5.0)
				matchesMask = mask.ravel().tolist()
				# h,w = img.shape
				pts = np.float32([ [0,0],[0,h-1],[w-1,h-1],[w-1,0] ]).reshape(-1,1,2)
				dst = cv2.perspectiveTransform(pts,M)
				ref_img_match = cv2.polylines(ref_img,[np.int32(dst)],True,255,3, cv2.LINE_AA)
				#cv2.imwrite('/home/kikot/ROS/img_match.jpg', ref_img_match)
			else:
				print( "Not enough matches are found - {}/{}".format(len(good), MIN_MATCH_COUNT) )
				matchesMask = None

			draw_params = dict(matchColor = (0,255,0), # draw matches in green color
							         singlePointColor = None,
							         matchesMask = matchesMask, # draw only inliers
							         flags = 2)
			img_fin = cv2.drawMatches(img, kp, ref_img, ref_kp, good, None, **draw_params)
			#plt.imshow(img_fin, 'gray'),plt.show()
			cv2.imwrite('/home/kikot/ROS/final.jpg', img_fin)
			  
		else:
		  print('The number of markers is not ok:',len(ids))

	else:
		print('No markers found')

	
	
	## poisci rdeci krizec ----------
	kriz_img = cv2.imread('/home/kikot/ROS/krizec.png', 0)
	kriz_hist, kriz_bins = np.histogram(img.ravel(),256,[0,256])
	plt.hist(img.ravel(),256,[0,256]); plt.show()
	
	for i in range(0, h):
		for j in range(0, w):
			#preveri, ali je ta del znotraj vcrtane kroznice
			
			#preveri, ali ima vec rdece kot ostalo
			print("")
	
	# TODO
	# poiscemo krizec na sliki in ga preslikamo na zemljevid : dest = cv2.perspectiveTransform(krizec,M)
	
	## objavi lokacijo krizca na zemljevidu ----------
	
	# TODO
	
	print("Koncano")

def main():
	#rospy.init_node("read_map")
	#service = rospy.Service('read_map', GetLocation, read_map_from_img)
	read_map_from_img()

	'''
	try:
		rospy.spin()
	except KeyboardInterrupt:
		print('Shutting down')
	'''

if __name__ == '__main__':
    main()
