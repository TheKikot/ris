#!/usr/bin/env python

import os
import rospy
import actionlib
from actionlib_msgs.msg import GoalStatus
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
from geometry_msgs.msg import Quaternion, PoseWithCovarianceStamped
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
	
def goToCircle(posXCircle, posYCircle):
	global posX, posY, posZ, rotW, rotZ, goalcircle, newCircle

	print("posXCircle: ", posXCircle)
	print("posYCircle: ", posYCircle)
	print("posX: ", posX)
	print("posY: ", posY)

	#razX = (posXCircle - posX) * 0.5 + posXCircle
	#razY = (posYCircle - posY) * 0.5 + posXCircle
	
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
	'''
	goal_state = ac.get_state()
	
	while (not goal_state == GoalStatus.SUCCEEDED):
		print("waiting to approach circle")
		ac.wait_for_result(rospy.Duration(0.5))
		goal_state = ac.get_state()
	
	ac.send_goal(goalk)
	print("sent new destination")
	while (not goal_state == GoalStatus.SUCCEEDED):
		print("approaching circle")
		ac.wait_for_result(rospy.Duration(0.5))
		goal_state = ac.get_state()
		'''
		
	newCircle = 1
	return


def addLocation(data):
	#a = 0.0 + data.pose.position.x
	#b = 0.0 + data.pose.position.y
	#ringLocations.append([data.pose.position.x, data.pose.position.y])
	global seq
	#global wantsToCheckCircle
	#wantsToCheckCircle = 0

			
	for i in ringLocationsX:
		if abs(i-data.pose.position.x) < 1.5:
			return
	#wantsToCheckCircle = 1
	ringLocationsX.append(data.pose.position.x)
	ringLocationsY.append(data.pose.position.y)
	
	print("before calling go to circle")
	#goToCircle(data.pose.position.x, data.pose.position.y)
	print("after calling go to circle")
	print(ringLocationsX)
	return




goal_state = GoalStatus.LOST

rospy.init_node('map_navigation', anonymous=False)

ac = actionlib.SimpleActionClient("move_base", MoveBaseAction)
rospy.Subscriber('markers', Marker, addLocation)
rospy.Subscriber('amcl_pose', PoseWithCovarianceStamped, updatePosition)
# subscriber za laser scan
#rospy.Subscriber('', )
ringLocationsX = []
ringLocationsY = []
seq = -1



while(not ac.wait_for_server(rospy.Duration.from_sec(2.0))):
              rospy.loginfo("Waiting for the move_base action server to come up")

'''

goal = []



goalk = MoveBaseGoal()
#0
#Sending a goal to the to a certain position in the map
goalk.target_pose.header.frame_id = "map"
goalk.target_pose.header.stamp = rospy.Time.now()
goalk.target_pose.pose.position.x = 0.4
goalk.target_pose.pose.position.y = -1.65
goalk.target_pose.pose.orientation.w = 0.336

goal.append(goalk)
goalk = MoveBaseGoal()
#1
#Sending a goal to the to a certain position in the map
goalk.target_pose.header.frame_id = "map"
goalk.target_pose.header.stamp = rospy.Time.now()
goalk.target_pose.pose.position.x = 0.25
goalk.target_pose.pose.position.y = -0.66
goalk.target_pose.pose.orientation.z = 0.91
goalk.target_pose.pose.orientation.w = 0.084

goal.append(goalk)

goalk = MoveBaseGoal()

goalk.target_pose.header.frame_id = "map"
goalk.target_pose.header.stamp = rospy.Time.now()
goalk.target_pose.pose.position.x = -1.284
goalk.target_pose.pose.position.y = -1.581
goalk.target_pose.pose.orientation.z = -0.171
goalk.target_pose.pose.orientation.w = 0.985

goal.append(goalk)

goalk = MoveBaseGoal()

goalk.target_pose.header.frame_id = "map"
goalk.target_pose.header.stamp = rospy.Time.now()
goalk.target_pose.pose.position.x = -0.719
goalk.target_pose.pose.position.y = -2.595
goalk.target_pose.pose.orientation.z = -0.466
goalk.target_pose.pose.orientation.w = 0.885
goal.append(goalk)

goalk = MoveBaseGoal()

goalk.target_pose.header.frame_id = "map"
goalk.target_pose.header.stamp = rospy.Time.now()
goalk.target_pose.pose.position.x = -1.377
goalk.target_pose.pose.position.y = -3.183
goalk.target_pose.pose.orientation.z = -0.959
goalk.target_pose.pose.orientation.w = 0.284
goal.append(goalk)

goalk = MoveBaseGoal()

goalk.target_pose.header.frame_id = "map"
goalk.target_pose.header.stamp = rospy.Time.now()
goalk.target_pose.pose.position.x = -2.420
goalk.target_pose.pose.position.y = -2.850
goalk.target_pose.pose.orientation.z = 0.917
goalk.target_pose.pose.orientation.w = 0.398
goal.append(goalk)



goalk = MoveBaseGoal()

goalk.target_pose.header.frame_id = "map"
goalk.target_pose.header.stamp = rospy.Time.now()
goalk.target_pose.pose.position.x = -2.994
goalk.target_pose.pose.position.y = -2.080
goalk.target_pose.pose.orientation.z = 0.897
goalk.target_pose.pose.orientation.w = 0.442
goal.append(goalk)

'''

ringsCollected = 0
goal = MoveBaseGoal()

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
			
			qOrg = [0, 0, goal.target_pose.pose.orientation.z, goal.target_pose.pose.orientation.z]
			
			(x, y, z) = euler_from_quaternion(qOrg)
			
			# turning sequence
			for j in range(0,8):
				# turning
				print("turn")		
				
				q = quaternion_from_euler(0, 0, z + j * (3.14/4.0))
				
				goal.target_pose.pose.orientation.z = q[2]
				goal.target_pose.pose.orientation.w = q[3]
				# got to position
    				rospy.loginfo("Sending goal")
				#rospy.loginfo(goal[i].target_pose.pose.position.x)
				ac.send_goal(goal)
				goal_state = GoalStatus.PENDING
				while (not goal_state == GoalStatus.SUCCEEDED):
					ac.wait_for_result(rospy.Duration(0.5))
					goal_state = ac.get_state()
					
				rospy.loginfo("The turn was reached!")
				# get image
				rospy.wait_for_service('get_ring_location')
				try:
						get_ring_location = rospy.ServiceProxy('get_ring_location', GetLocation)
						get_ring_location()
						if(newCircle == 1):
							newCircle = 0
							print(goalcircle)
							ac.send_goal(goalcircle)
							goal_state = GoalStatus.PENDING
							while (not goal_state == GoalStatus.SUCCEEDED):
								ac.wait_for_result(rospy.Duration(0.5))
								goal_state = ac.get_state()
							os.system("rosrun sound_play say.py 'score' ")
							circleCounter += 1
							if circleCounter >= 3:
								sys.exit()
				except rospy.ServiceException, e:
						print "Service call failed: %s"%e				
						
						
						
						
GoalStatus.SUCCEEDED




