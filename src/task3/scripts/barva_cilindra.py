#!/usr/bin/env python
from __future__ import print_function

import random
import sys
import rospy
import cv2
import math
import numpy as np
import tf2_geometry_msgs
import tf2_ros
from sensor_msgs.msg import Image
from geometry_msgs.msg import PointStamped, Vector3, Pose
from cv_bridge import CvBridge, CvBridgeError
from visualization_msgs.msg import Marker, MarkerArray
from std_msgs.msg import ColorRGBA
from task3.srv import *


callFunction = False
location = GetColorRequest()

def color_handler(position):
	global callFunction
	global location
	callFunction = True
	location = position
	
	#print('I got a new image!')
  data = rospy.wait_for_message('/camera/rgb/image_raw', Image)
  try:
      print('converting image')
      cv_image = self.bridge.imgmsg_to_cv2(data, 'bgr8')
      print('image converted!')
  except CvBridgeError, e:
      print(e)
	
	
	# poiscemo cilinder na sliki
	
	kot = math.atan2(location.cam_X,location.cam_Y)
	print(kot)	
	
	# 640x480
	odmik = 320 + 525/45 * kot
	
	crop = cv_image[240:250, (odmik-10):(odmik+10)]
	cv2.imwrite('crop.jpeg', cv_image)
	
	print("omogocam zaznavo barve")
	return 0


def check_color(image):
	global callFunction
	global location
	if(callFunction):
		#print("klicem funkcijo")
		
		
		
		
		# preberi barvo
		
		callFunction = False
	else:
		rospy.sleep(1)


def main():
	global location
	# print("setting up node")
	rospy.init_node('cylinder_color', anonymous=False)
	
	points_sub = rospy.Subscriber("/camera/rgb/image_raw", Image, check_color)
	call_srv = rospy.Service('cylinder_color', GetColor, color_handler)
	
	try:
		rospy.spin()
	except KeyboardInterrupt:
	  print("Shutting down")



if __name__ == '__main__':
	main()
	
