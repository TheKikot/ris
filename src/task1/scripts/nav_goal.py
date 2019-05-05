#!/usr/bin/env python

import os
import rospy
import actionlib
from actionlib_msgs.msg import GoalStatus
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
from geometry_msgs.msg import Quaternion, PoseWithCovarianceStamped
from sensor_msgs.msg import LaserScan
from tf.transformations import quaternion_from_euler, euler_from_quaternion
from visualization_msgs.msg import Marker, MarkerArray
from task1.srv import *
from sound_play.msg import SoundRequest
from sound_play.libsoundplay import SoundClient


#seq = -1
#wantsToCheckCircle = 0
#readyToCheckCircle = 0

posX = 0
posY = 0
posZ = 0
rotW = 0
rotZ = 0
# razdalja, na kateri lahko poberemo obroc
odmik = 0.2

circleCounter = 0
newCircle = 0
goalcircle = MoveBaseGoal()

def updatePosition(pos):
	global posX, posY, posZ, rotW, rotZ
	posX = pos.pose.pose.position.x
	posY = pos.pose.pose.position.y
	posZ = pos.pose.pose.position.z
	rotW = pos.pose.pose.orientation.w
	rotZ = pos.pose.pose.orientation.z
	

def addLocation(data):
	
	print("picking up ring")
	pickUpRing(data.pose.position.x, data.pose.position.y)
	return

def pickUpRing(ringX, ringY):
	
	# vektor v smeri obroca v x in y koordinatah
	razX =  posX - ringX
	razY =  posY - ringY
	
	# vektor, pravokoten na vektor v smeri obroca
	
	normX = - (razY / razX)
	normY = 1
	
	dolzina = (normX**2 + normY**2)**(1/2)
	
	normX = normX / dolzina
	normY = normY / dolzina
	
	ortX = normY * odmik
	ortY = normX * odmik
	
	goToPosition(ringX, ortX, ringY, ortY)
	
	return


def goToPosition(ringX, ortX, ringY, ortY):
	pos1X = ringX+ortX
	pos1Y = ringY+ortY
	pos2X = ringX-ortX
	pos2Y = ringY-ortY
	
	# izracunamo kote
	qOrg = [0, 0, rotZ, rotW]
			
	(x, y, z) = euler_from_quaternion(qOrg)
	
	q1 = quaternion_from_euler(0, 0, z - (3.14/2.0))
	q2 = quaternion_from_euler(0, 0, z + (3.14/2.0))

	goalk = MoveBaseGoal()
	
	goalk.target_pose.header.frame_id = "map"
	goalk.target_pose.header.stamp = rospy.Time.now()
	goalk.target_pose.pose.position.x = pos1X
	goalk.target_pose.pose.position.y = pos1Y
	goalk.target_pose.pose.orientation.z = q1[2]
	goalk.target_pose.pose.orientation.w = q1[3]
	
	print("first goal")
	print("pending:")
	print(GoalStatus.PENDING)
	print("active:")
	print(GoalStatus.ACTIVE)
	print("success:")
	print(GoalStatus.SUCCEEDED)
	print("aborted:")
	print(GoalStatus.ABORTED)
	
	
	ac.send_goal(goalk)
	
	goal_state = ac.get_state()
	while (goal_state == GoalStatus.PENDING or goal_state == GoalStatus.ACTIVE):
		print(goal_state)
		ac.wait_for_result(rospy.Duration(0.5))
		goal_state = ac.get_state()
	
	print(goal_state)
	
	print("next goal")
	
	goalk.target_pose.header.stamp = rospy.Time.now()
	goalk.target_pose.pose.position.x = pos2X
	goalk.target_pose.pose.position.y = pos2Y
	goalk.target_pose.pose.orientation.z = q2[2]
	goalk.target_pose.pose.orientation.w = q2[3]
	
	ac.send_goal(goalk)
	
	goal_state = ac.get_state()
	while (goal_state == GoalStatus.PENDING or goal_state == GoalStatus.ACTIVE):
		print(goal_state)
		ac.wait_for_result(rospy.Duration(0.5))
		goal_state = ac.get_state()

	print(goal_state)	
	print("finished")
	return



goal_state = GoalStatus.LOST

rospy.init_node('map_navigation', anonymous=False)

ac = actionlib.SimpleActionClient("move_base", MoveBaseAction)
rospy.Subscriber('markers', Marker, addLocation)
rospy.Subscriber('amcl_pose', PoseWithCovarianceStamped, updatePosition)
# subscriber za laser scan
#rospy.Subscriber('', )



while(not ac.wait_for_server(rospy.Duration.from_sec(2.0))):
              rospy.loginfo("Waiting for the move_base action server to come up")



ringsCollected = 0
goal = MoveBaseGoal()

rospy.wait_for_service('get_ring_location')
try:
	get_ring_location = rospy.ServiceProxy('get_ring_location', GetLocation)
	get_ring_location()
except rospy.ServiceException, e:
	print "Service call failed: %s"%e
	
	
try:
	rospy.spin()
except KeyboardInterrupt:
  print("Shutting down")
#while(True):
#	a=1
'''
while ringsCollected < 3:
	rospy.loginfo("Searching for a place to go")
	
	
	
	goal = getGoal()

	rospy.loginfo("Sending goal")
	#rospy.loginfo(goal[i].target_pose.pose.position.x)
	ac.send_goal(goal)
	goal_state = GoalStatus.PENDING
	while (not goal_state == GoalStatus.SUCCEEDED):

		ac.wait_for_result(rospy.Duration(2))
		goal_state = ac.get_state()
		#Possible States Are: PENDING, ACTIVE, RECALLED, REJECTED, PREEMPTED, ABORTED, SUCCEEDED, LOST.

		if not goal_state == GoalStatus.SUCCEEDED:
			rospy.loginfo("The goal has not been reached yet! Checking again in 2s.")
		else:
			rospy.loginfo("The goal was reached!")
			
						
						
GoalStatus.SUCCEEDED

'''


