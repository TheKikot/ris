#!/usr/bin/env python

import sys
import rospy
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
from geometry_msgs.msg import Twist, Quaternion, PoseWithCovarianceStamped
from exercise6.msg import *
import actionlib
from actionlib_msgs.msg import GoalStatus

#from task1.srv import *
posX = 0
posY = 0
posZ = 0
rotW = 0
rotZ = 0

def updatePosition(pos):
	global posX, posY, posZ, rotW, rotZ
	posX = pos.pose.pose.position.x
	posY = pos.pose.pose.position.y
	posZ = pos.pose.pose.position.z
	rotW = pos.pose.pose.orientation.w
	rotZ = pos.pose.pose.orientation.z

def goToCircle(posXCircle, posYCircle):
	global posX, posY, posZ, rotW, rotZ#, goalcircle, newCircle

	print("posXCircle: ", posXCircle)
	print("posYCircle: ", posYCircle)
	print("posX: ", posX)
	print("posY: ", posY)
	
	razX = -(posXCircle - posX)
	razY = -(posYCircle - posY)
	
	raz = (razX**2 + razY**2)**(1/2)
	if(raz > 1):
		return
	razX = razX / raz
	razY = razY / raz
	
	razX = (razX*0.7) + posXCircle
	razY = (razY*0.7) + posYCircle
	
	print("razX: ", razX)
	print("razY: ", razY)
	
	print("preparing new destination")
	#nov destination
	goalcircle = MoveBaseGoal()

	#Sending a goal to the to a certain position in the map
	goalcircle.target_pose.header.frame_id = "map"
	goalcircle.target_pose.header.stamp = rospy.Time.now()
	goalcircle.target_pose.pose.position.x = razX
	goalcircle.target_pose.pose.position.y = razY
	goalcircle.target_pose.pose.orientation.x = 0
	goalcircle.target_pose.pose.orientation.y = 0
	goalcircle.target_pose.pose.orientation.z = rotZ
	goalcircle.target_pose.pose.orientation.w = rotW
	
	goal_state = ac.get_state()
	
	while (not goal_state == GoalStatus.SUCCEEDED):
		print("waiting to approach circle")
		ac.wait_for_result(rospy.Duration(0.5))
		goal_state = ac.get_state()
	
	ac.send_goal(goalk)
	print("sent new destination")
	'''
	while (not goal_state == GoalStatus.SUCCEEDED):
		print("approaching circle")
		ac.wait_for_result(rospy.Duration(0.5))
		goal_state = ac.get_state()
	'''

	return

def get_ring(location):
	# get ring location
	#	print(location.x, location.y)
	goToCircle(location.x, location.y)
	pub = rospy.Publisher('/cmd_vel', Twist)
	r = rospy.Rate(5) #10hz
	
	twist_msg = Twist()
	twist_msg.linear.x = 1.0
	twist_msg.linear.y = 0.0
	twist_msg.linear.z = 0.0
	twist_msg.angular.x = 0.0
	twist_msg.angular.y = 0.0
	twist_msg.angular.z = 0.0
	
	
	time = 0.0
	while time < 1.1:	
		pub.publish(twist_msg)
		r.sleep()
		time += 0.2
	
	twist_msg.linear.x = 0.0
	pub.publish(twist_msg)
	
	

if __name__ == "__main__":
	
	rospy.init_node('ring_collection', anonymous=False)
	ac = actionlib.SimpleActionClient("move_base", MoveBaseAction)
	rospy.Subscriber('/grab_3d_ring', RingLocation, get_ring)
	rospy.Subscriber('amcl_pose', PoseWithCovarianceStamped, updatePosition)
	try:
		rospy.spin()
	except KeyboardInterrupt:
		print("Shutting down")
