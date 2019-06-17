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

def read_map_from_img():
	# parameter za spodnjo mejo iskanja projekcije
	MIN_MATCH_COUNT = 10
	
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
	
	# ce algoritem ne bo dovolj robusten, dodaj tu homografijo z markerji!
	print("berem sliko")
	
	'''
	# SIFT
	img = cv2.imread('/home/kikot/ROS/map_pictures/map_red.jpg')
	gray= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
	print("1")
	sift = cv2.xfeatures2d.SIFT_create()
	print("2")
	kp = sift.detect(gray,None)
	print("3")
	img=cv2.drawKeypoints(gray,kp,img)
	print("4")	
	cv2.imwrite('/home/kikot/ROS/map_pictures/sift_keypoints.jpg',img)
	print("5")
	'''
	
	## SURF ----------
	
	img = cv2.imread('/home/kikot/ROS/map_pictures/map_blue.jpg', 0)
	h,w = img.shape
	img = img[0+(h/4):(3*h/4), 0+(w/4):(3*w/4)]
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
	cv2.imwrite('/home/kikot/ROS/sift_keypoints.jpg',ref_img_kp)
	
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
		cv2.imwrite('/home/kikot/ROS/img_match.jpg', ref_img_match)
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
	
	## poisci rdeci krizec ----------
	
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
