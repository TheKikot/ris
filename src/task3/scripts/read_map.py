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
	## preberi sliko
	
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
	
	# SURF
	
	img = cv2.imread('/home/kikot/ROS/map_pictures/map_red.jpg', 0)
	print("1")
	surf = cv2.xfeatures2d.SURF_create(40000)
	print("2")
	kp, des = surf.detectAndCompute(img,None)
	print("3")
	img2 = cv2.drawKeypoints(img,kp,None,(255,0,0),4)
	print("4")
	plt.imshow(img2),plt.show()
	## ustvari deskriptor
	
	## poisci homografijo
	
	## poisci rdeci krizec
	
	## objavi lokacijo krizca na zemljevidu
	
	
	
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
