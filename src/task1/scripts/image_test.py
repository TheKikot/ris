#!/usr/bin/env python
from __future__ import print_function

import os
import sys
import rospy
import cv2
import numpy as np
import tf2_geometry_msgs
import tf2_ros
from sensor_msgs.msg import Image
from geometry_msgs.msg import PointStamped, Vector3, Pose
from cv_bridge import CvBridge, CvBridgeError
from visualization_msgs.msg import Marker, MarkerArray
from std_msgs.msg import ColorRGBA
from task1.srv import *



rospy.init_node("image_test")
bridge = CvBridge()
img_pub = rospy.Publisher("camera/rgb/image_raw", Image, queue_size=1)
depth_pub = rospy.Publisher("camera/depth_registered/image_raw", Image, queue_size=1)


try:
	
	print('reading image')
	imgdata = cv2.imread("circles_camera_image_6.jpeg")
	depthdata = cv2.imread("circles_camera_image_6_threshed.jpeg", cv2.IMREAD_GRAYSCALE)
	color_image = bridge.cv2_to_imgmsg(imgdata)
	depth_image = bridge.cv2_to_imgmsg(depthdata)
	print('image converted!')
	img_pub.publish(color_image)
	depth_pub.publish(depth_image)	
	#rospy.spin()
	#os.system("/home/kikot/ROS/src/task1/scripts/ring_test.py")
	
except KeyboardInterrupt:
  print("Shutting down")


	
	
	
	
