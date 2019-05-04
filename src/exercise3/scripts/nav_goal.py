#!/usr/bin/env python

import rospy
import actionlib
from actionlib_msgs.msg import GoalStatus
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal

goal_state = GoalStatus.LOST

rospy.init_node('map_navigation', anonymous=False)

ac = actionlib.SimpleActionClient("move_base", MoveBaseAction)

while(not ac.wait_for_server(rospy.Duration.from_sec(2.0))):
              rospy.loginfo("Waiting for the move_base action server to come up")

goal = []

goalk = MoveBaseGoal()

#Sending a goal to the to a certain position in the map
goalk.target_pose.header.frame_id = "map"
goalk.target_pose.header.stamp = rospy.Time.now()
goalk.target_pose.pose.position.x = 0.54
goalk.target_pose.pose.position.y = 2.87
goalk.target_pose.pose.orientation.w = 0.336

goal.append(goalk)
goalk = MoveBaseGoal()

#Sending a goal to the to a certain position in the map
goalk.target_pose.header.frame_id = "map"
goalk.target_pose.header.stamp = rospy.Time.now()
goalk.target_pose.pose.position.x = -0.697
goalk.target_pose.pose.position.y = 3.909
goalk.target_pose.pose.orientation.w = 0.284

goal.append(goalk)
goalk = MoveBaseGoal()

goalk.target_pose.header.frame_id = "map"
goalk.target_pose.header.stamp = rospy.Time.now()
goalk.target_pose.pose.position.x = -1.74
goalk.target_pose.pose.position.y = 2.63
goalk.target_pose.pose.orientation.w = 0.983

goal.append(goalk)
goalk = MoveBaseGoal()

goalk.target_pose.header.frame_id = "map"
goalk.target_pose.header.stamp = rospy.Time.now()
goalk.target_pose.pose.position.x = -1.296
goalk.target_pose.pose.position.y = 0.908
goalk.target_pose.pose.orientation.w = 0.983

goal.append(goalk)
goalk = MoveBaseGoal()

goalk.target_pose.header.frame_id = "map"
goalk.target_pose.header.stamp = rospy.Time.now()
goalk.target_pose.pose.position.x = 1.201
goalk.target_pose.pose.position.y = 1.424
goalk.target_pose.pose.orientation.w = 0.475
goal.append(goalk)

for i in range(0,5):
	rospy.loginfo("Sending goal")
	rospy.loginfo(goal[i].target_pose.pose.position.x)
	ac.send_goal(goal[i])
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
