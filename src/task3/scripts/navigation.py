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
	#preberi podatke o zemljevidu
	meta = mapData.info
	staticMap = mapData.data
	sirina = meta.width
	visina = meta.height
	resolucija = meta.resolution
	# dimenzije so naceloma 75 x 100
	# downsize je količnik oz. faktor pomanjšanja
	downsize = 5
	
	grid = [[0] * (visina/downsize) for i in range(0,	sirina/downsize)]
	
	#print("visina: ", visina)
	
	for i in range(0, sirina):
		#print("i: ",i)
		for j in range(0, visina):
			mapval = staticMap[i*visina + j]
			if mapval == 0:
				# prosto
				grid[i/downsize][j/downsize] += 0
			elif mapval == 100:
				# zasedeno
				grid[i/downsize][j/downsize] += 1
			elif mapval == -1:
				# neznano
				grid[i/downsize][j/downsize] = -1
			else:
				# napaka
				print("Nepričakovana vrednost na zemljevidu!")
	
	#print cele mreže
	'''
	for k in grid:
		print(" ")
		print(k)
	'''
	


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

