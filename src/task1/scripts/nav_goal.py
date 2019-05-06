#!/usr/bin/env python

import os
import rospy
import actionlib
from actionlib_msgs.msg import GoalStatus
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
from geometry_msgs.msg import Twist, Quaternion, PoseWithCovarianceStamped
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
twisting = 0
processing = 0

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
	global newCircle
	newCircle = 1
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
	goalk.target_pose.pose.orientation.z = q2[2]
	goalk.target_pose.pose.orientation.w = q2[3]
	
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
		ac.wait_for_result(rospy.Duration(0.5))
		goal_state = ac.get_state()
	
	if(goal_state == GoalStatus.SUCCEEDED):
		grabRing()
		grabRing()
	else:
		print("first goal failed")
		print("alternative goal")
	
		goalk.target_pose.header.stamp = rospy.Time.now()
		goalk.target_pose.pose.position.x = pos2X
		goalk.target_pose.pose.position.y = pos2Y
		goalk.target_pose.pose.orientation.z = q1[2]
		goalk.target_pose.pose.orientation.w = q1[3]
	
		ac.send_goal(goalk)
	
		goal_state = ac.get_state()
		while (goal_state == GoalStatus.PENDING or goal_state == GoalStatus.ACTIVE):
			ac.wait_for_result(rospy.Duration(0.5))
			goal_state = ac.get_state()

		if(goal_state == GoalStatus.SUCCEEDED):
			grabRing()
			grabRing()
		else:
			print("failed both times, killme")	
		
		
	print("finished")
	global twisting, newCircle
	twisting = 0
	newCircle = 0
	return


def grabRing():
	global twisting
	twisting = 1
	pub = rospy.Publisher('/mobile_base/commands/velocity', Twist, queue_size=10)
	r = rospy.Rate(5) #
	
	twist_msg = Twist()
	twist_msg.linear.x = 0.05
	twist_msg.linear.y = 0.0
	twist_msg.linear.z = 0.0
	twist_msg.angular.x = 0.0
	twist_msg.angular.y = 0.0
	twist_msg.angular.z = 0.0
	
	
	time = 0.0
	while time < 0.7:	
		pub.publish(twist_msg)
		r.sleep()
		time += 0.1
	
	twist_msg.linear.x = 0.0
	pub.publish(twist_msg)
	
	twist_msg.angular.z = 1.15
	
	time = 0.0
	while time < 2.7:	
		pub.publish(twist_msg)
		r.sleep()
		time += 0.1
	
	twist_msg.angular.z = 0.0
	pub.publish(twist_msg)
	
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





	
	
goal = []
goalk = MoveBaseGoal()

goalk.target_pose.header.frame_id = "map"
goalk.target_pose.header.stamp = rospy.Time.now()
goalk.target_pose.pose.position.x = -1.720
goalk.target_pose.pose.position.y = -3.204
goalk.target_pose.pose.orientation.z = 0.8717
goalk.target_pose.pose.orientation.w = 0.49

goal.append(goalk)

goalk = MoveBaseGoal()

goalk.target_pose.header.frame_id = "map"
goalk.target_pose.header.stamp = rospy.Time.now()
goalk.target_pose.pose.position.x = -2.305
goalk.target_pose.pose.position.y = -3.154
goalk.target_pose.pose.orientation.z = 0.2275
goalk.target_pose.pose.orientation.w = 0.9737

goal.append(goalk)

goalk = MoveBaseGoal()

goalk.target_pose.header.frame_id = "map"
goalk.target_pose.header.stamp = rospy.Time.now()
goalk.target_pose.pose.position.x = -0.8342
goalk.target_pose.pose.position.y = -2.752
goalk.target_pose.pose.orientation.z = 0.860
goalk.target_pose.pose.orientation.w = 0.5102

goal.append(goalk)

goalk = MoveBaseGoal()

goalk.target_pose.header.frame_id = "map"
goalk.target_pose.header.stamp = rospy.Time.now()
goalk.target_pose.pose.position.x = -1.8644
goalk.target_pose.pose.position.y = -1.2515
goalk.target_pose.pose.orientation.z = 0.3529
goalk.target_pose.pose.orientation.w = 0.9356

goal.append(goalk)

goalk = MoveBaseGoal()

goalk.target_pose.header.frame_id = "map"
goalk.target_pose.header.stamp = rospy.Time.now()
goalk.target_pose.pose.position.x = -1.016
goalk.target_pose.pose.position.y = -1.1712
goalk.target_pose.pose.orientation.z = 0.2485
goalk.target_pose.pose.orientation.w = 0.9686

goal.append(goalk)


'''	
goalk = MoveBaseGoal()

goalk.target_pose.header.frame_id = "map"
goalk.target_pose.header.stamp = rospy.Time.now()
goalk.target_pose.pose.position.x = -0.3139
goalk.target_pose.pose.position.y = -1.7228
goalk.target_pose.pose.orientation.z = 0.4073
goalk.target_pose.pose.orientation.w = 0.9132

goal.append(goalk)
'''
	
goalk = MoveBaseGoal()

goalk.target_pose.header.frame_id = "map"
goalk.target_pose.header.stamp = rospy.Time.now()
goalk.target_pose.pose.position.x = 0.6023
goalk.target_pose.pose.position.y = -1.2186
goalk.target_pose.pose.orientation.z = 0.9136
goalk.target_pose.pose.orientation.w = 0.4065

goal.append(goalk)	
'''	
goalk = MoveBaseGoal()

goalk.target_pose.header.frame_id = "map"
goalk.target_pose.header.stamp = rospy.Time.now()
goalk.target_pose.pose.position.x = -0.9593
goalk.target_pose.pose.position.y = -0.7441
goalk.target_pose.pose.orientation.z = -0.339
goalk.target_pose.pose.orientation.w = 0.9407

goal.append(goalk)
'''
goalk = MoveBaseGoal()

goalk.target_pose.header.frame_id = "map"
goalk.target_pose.header.stamp = rospy.Time.now()
goalk.target_pose.pose.position.x = 0.4636
goalk.target_pose.pose.position.y = -0.8139
goalk.target_pose.pose.orientation.z = -0.9018
goalk.target_pose.pose.orientation.w = 0.4319

goal.append(goalk)

goalk = MoveBaseGoal()

goalk.target_pose.header.frame_id = "map"
goalk.target_pose.header.stamp = rospy.Time.now()
goalk.target_pose.pose.position.x = 0.0305
goalk.target_pose.pose.position.y = -0.1618
goalk.target_pose.pose.orientation.z = -0.8938
goalk.target_pose.pose.orientation.w = 0.4484

goal.append(goalk)


for i in range(0,7):

	while(twisting == 1 or newCircle == 1):
		continue
	
	#lahko posljem naslednjo lokacijo
	rospy.loginfo("Sending goal")

	ac.send_goal(goal[i])
	goal_state = GoalStatus.PENDING
	
	#waiting to arrive to destination
	while (not goal_state == GoalStatus.SUCCEEDED):
		ac.wait_for_result(rospy.Duration(2))
		goal_state = ac.get_state()
	#at destination
		
	#getting picture, analyzing, getting any rings
	rospy.wait_for_service('get_ring_location')
	try:
		get_ring_location = rospy.ServiceProxy('get_ring_location', GetLocation)
		get_ring_location()
	except rospy.ServiceException, e:
		print "Service call failed: %s"%e

					
						
GoalStatus.SUCCEEDED




