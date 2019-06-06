#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import print_function

#import random
#import sys
import rospy
import cv2
import numpy as np
import tf2_geometry_msgs
import tf2_ros
from nav_msgs.srv import GetMap
from nav_msgs.msg import OccupancyGrid
#from sensor_msgs.msg import Image
#from geometry_msgs.msg import PointStamped, Vector3, Pose
#from cv_bridge import CvBridge, CvBridgeError
#from visualization_msgs.msg import Marker, MarkerArray
#from std_msgs.msg import ColorRGBA
#from task3.srv import *

def read_map(staticMap):
	print(len(staticMap)/ 512)

def main():
	rospy.init_node('navigation', anonymous=False)
	rospy.wait_for_service('static_map')
	try:
		mapService = rospy.ServiceProxy('static_map', GetMap)
		staticMap = mapService().map.data
		read_map(staticMap)
	except Exception, e:
		print(e)

if __name__ == '__main__':
	main()

