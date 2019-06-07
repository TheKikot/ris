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
from nav_msgs.msg import OccupancyGrid, MapMetaData
#from sensor_msgs.msg import Image
#from geometry_msgs.msg import PointStamped, Vector3, Pose
#from cv_bridge import CvBridge, CvBridgeError
#from visualization_msgs.msg import Marker, MarkerArray
#from std_msgs.msg import ColorRGBA
#from task3.srv import *

def read_map(mapData):
	meta = mapData.info
	staticMap = mapData.data
	# dimenzije : 75 x 100
	for i in range(0,100):
		print(staticMap[i*75+0:i*75+75])
	

def main():
	rospy.init_node('navigation', anonymous=False)
	rospy.wait_for_service('static_map')
	try:
		mapService = rospy.ServiceProxy('static_map', GetMap)
		mapData = mapService().map
		read_map(mapData)
	except Exception, e:
		print(e)

if __name__ == '__main__':
	main()

