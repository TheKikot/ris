#!/usr/bin/env python
from __future__ import print_function

#import random
#import sys
import rospy
#import cv2
import math
#import numpy as np
import tf2_geometry_msgs
import tf2_ros
#from sensor_msgs.msg import Image
#from geometry_msgs.msg import PointStamped, Vector3, Pose
from nav_msgs.srv import GetMap
from nav_msgs.msg import OccupancyGrid, MapMetaData
#from cv_bridge import CvBridge, CvBridgeError
#from visualization_msgs.msg import Marker, MarkerArray
#from std_msgs.msg import ColorRGBA
from task3.srv import *

global mapData

# cSe je prosto, vrne 1, sicer 0
def cir_handler(location):
	global mapData
	staticMap = mapData.data
	meta = mapData.info
	sirina = meta.width
	visina = meta.height
	resolucija = meta.resolution
	origX = meta.origin.position.x
	origY = meta.origin.position.y
#	origOrient = meta.origin.orientation

#	mapval = staticMap[i*visina + j]
#	goal.target_pose.pose.position.x = origX + resolucija * downsize * (x + 0.5)
#	goal.target_pose.pose.position.y = origY + resolucija * downsize * (y + 0.5)
	x = int( (location.map_X - origX) / resolucija )
	y = int( (location.map_Y - origY) / resolucija )
	
	for k in range(y-3, y+3):
		for l in range(x-3, x+3):
			if(y > sirina or y < 0 or x > visina or x < 0):
				#print("out of map")
				return 0
			elif(staticMap[k*visina + l] != 0):
				#print("occupied")
				return 0
			else:
				#print("free")
				continue
				
	
	return 1

	

def main():
	
	rospy.init_node('check_if_reachable_node', anonymous=False)
	
	rospy.wait_for_service('static_map')
	
	try:
		global mapData
		mapService = rospy.ServiceProxy('static_map', GetMap)
		mapData = mapService().map
		print("map saved!")
	except Exception, e:
		print(e)
	
	call_srv = rospy.Service('check_if_reachable', GetColor, cir_handler)
	
	try:
		rospy.spin()
	except KeyboardInterrupt:
	  print("Shutting down")



if __name__ == '__main__':
	main()
	
