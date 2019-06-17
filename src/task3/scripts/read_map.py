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
	img = cv2.imread('/home/kikot/ROS/map_pictures/map_red.jpg')
	
	# Initiate FAST object with default values
	fast = cv2.FastFeatureDetector()

	# find and draw the keypoints
	kp = fast.detect(img,None)
	img2 = cv2.drawKeypoints(img, kp, color=(255,0,0))

	# Print all default params
	print( "Threshold: ", fast.getInt('threshold') )
	print( "nonmaxSuppression: ", fast.getBool('nonmaxSuppression') )
	print( "neighborhood: ", fast.getInt('type') )
	print( "Total Keypoints with nonmaxSuppression: ", len(kp) )

	cv2.imwrite('fast_true.png',img2)

	# Disable nonmaxSuppression
	fast.setBool('nonmaxSuppression',0)
	kp = fast.detect(img,None)

	print( "Total Keypoints without nonmaxSuppression: ", len(kp) )

	img3 = cv2.drawKeypoints(img, kp, color=(255,0,0))

	cv2.imwrite('fast_false.png',img3)
	
	
	
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
