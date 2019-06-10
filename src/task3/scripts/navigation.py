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
import actionlib
from nav_msgs.srv import GetMap
from nav_msgs.msg import OccupancyGrid, MapMetaData
from actionlib_msgs.msg import GoalStatus
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
from geometry_msgs.msg import PointStamped, Vector3, Pose, Twist, Quaternion, PoseWithCovarianceStamped
from visualization_msgs.msg import Marker, MarkerArray
from std_msgs.msg import ColorRGBA
from tf.transformations import quaternion_from_euler, euler_from_quaternion
from task3.srv import *

def poslji_marker(origX, origY, resolucija, downsize, x, y, marker_id):
	marker = Marker()
	marker.header.stamp = rospy.Time.now()
	marker.header.frame_id = "map"
	marker.pose.position.x = origX + 1.0 * resolucija * downsize * x
	marker.pose.position.y = origY + 1.0 * resolucija * downsize * y
	marker.pose.position.z = 5.0
	marker.type = Marker.CUBE
	marker.action = Marker.ADD
	marker.frame_locked = False
	marker.lifetime = rospy.Duration.from_sec(10)
	marker.id = marker_id
	marker.scale = Vector3(0.1, 0.1, 0.1)
	marker.color = ColorRGBA(0, 1, 0, 1)
	print("posiljam marker")
	pubm.publish(marker)
	#print("marker poslan")

def poslji_cilj(origX, origY, origOrient, resolucija, downsize, x, y):

	goal = MoveBaseGoal()
	
	goal.target_pose.header.frame_id = "map" 
	goal.target_pose.header.stamp = rospy.Time.now()
	goal.target_pose.pose.position.x = origX + resolucija * downsize * (x + 0.5)
	goal.target_pose.pose.position.y = origY + resolucija * downsize * (y + 0.5)
	goal.target_pose.pose.orientation = origOrient
	print("pošiljam cilj: (", goal.target_pose.pose.position.x, ", ", goal.target_pose.pose.position.y, ")")
	ac.send_goal(goal)
	goal_state = ac.get_state()
	while (goal_state == GoalStatus.PENDING or goal_state == GoalStatus.ACTIVE):
		ac.wait_for_result(rospy.Duration(2.0))
		#print("goal_state: ", goal_state)
		goal_state = ac.get_state()
	print("goal_state_fin: ", goal_state)
	
	if (goal_state == 3) :
		for j in range(0,8):
			# turning
			print("turn, q = ", origOrient)		
	
			#(x, y, z) = euler_from_quaternion(origOrient)
			q = quaternion_from_euler(0, 0, origOrient.z + j * (3.14/4.0))

			goal.target_pose.pose.orientation.z = q[2]
			goal.target_pose.pose.orientation.w = q[3]
			# got to position
			#rospy.loginfo("Sending goal")
			#rospy.loginfo(goal[i].target_pose.pose.position.x)
			ac.send_goal(goal)
			goal_state = GoalStatus.PENDING
			while (goal_state == GoalStatus.PENDING or goal_state == GoalStatus.ACTIVE):
				ac.wait_for_result(rospy.Duration(2.0))
				#print("goal_state: ", goal_state)
				goal_state = ac.get_state()
			print("turn_state_fin: ", goal_state)
			
			# look for rings
			rospy.wait_for_service('get_ring_location')
			try:
				get_ring_location = rospy.ServiceProxy('get_ring_location', GetLocation)
				get_ring_location()
			except rospy.ServiceException, e:
				print ("Service call failed: %s"%e)
			
			# look for cylinders
			rospy.wait_for_service('detect_cylinder')
			try:
				get_cylinder_location = rospy.ServiceProxy('detect_cylinder', GetLocation)
				get_cylinder_location()
			except rospy.ServiceException, e:
				print ("Service call failed: %s"%e)

			rospy.sleep(7)
	

def read_map(mapData):
	# konstante
	cilj_odmik = 4
	cilj_step = 6

	# preberi podatke o zemljevidu
	meta = mapData.info
	staticMap = mapData.data
	sirina = meta.width
	visina = meta.height
	resolucija = meta.resolution
	origX = meta.origin.position.x
	origY = meta.origin.position.y
	origOrient = meta.origin.orientation
	# dimenzije so naceloma 75 x 100
	# downsize je količnik oz. faktor pomanjšanja
	# pri resoluciji 0.05 in faktorju 4 so celice velike 20cm (malo manj kot roomba)
	downsize = 4
	
	grid = [[0] * (visina/downsize) for i in range(0,	sirina/downsize)]
	
	#print("visina: ", visina, "sirina", sirina)
	
	for i in range(0, sirina):
		#print("i: ",i)
		for j in range(0, visina):
			mapval = staticMap[i*visina + j]
			#print(i,", ",j)
			if mapval == 0:
				# prosto
				grid[i/downsize][j/downsize] += 0
			elif mapval == 100:
				# zasedeno
				grid[i/downsize][j/downsize] = 1
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
	
	print("origin: ", origX, ", ", origY)
	
	for k in range(1, sirina/downsize-1, cilj_step):
		for l in range(1+ cilj_odmik, visina/downsize-1, cilj_step):
			if(grid[k][l] == 0 and grid[k+1][l] == 0 and grid[k-1][l] == 0 and grid[k][l+1] == 0 and grid[k][l-1] == 0):
				poslji_cilj(origX, origY, origOrient, resolucija, downsize, l, k)
				#poslji_marker(origX, origY, resolucija, downsize, k, l, k+l)
	masterService()




## ZAČETEK SKRIPTE

# INFO PRINT
#print("pending:")
#print(GoalStatus.PENDING) # 0
#print("active:")
#print(GoalStatus.ACTIVE) # 1
#print("success:")
#print(GoalStatus.SUCCEEDED) # 3
#print("aborted:")
#print(GoalStatus.ABORTED) # 4

# INICIALIZACIJA
rospy.init_node('navigation', anonymous=False)
rospy.wait_for_service('static_map')
rospy.wait_for_service('start_master')
ac = actionlib.SimpleActionClient("move_base", MoveBaseAction)
pubm = rospy.Publisher('goal_marker', Marker, queue_size=100)

while(not ac.wait_for_server(rospy.Duration.from_sec(3.0))):
              rospy.loginfo("Waiting for the move_base action server to come up")
# ZAGON
try:
	mapService = rospy.ServiceProxy('static_map', GetMap)
	masterService = rospy.ServiceProxy('start_master', GetLocation)
	mapData = mapService().map
	read_map(mapData)
except Exception, e:
	print(e)


# KONEC
