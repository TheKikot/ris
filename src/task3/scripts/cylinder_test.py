#!/usr/bin/env python

import sys
import rospy
from task3.srv import *
from std_msgs.msg import String



def main():
	#print("setting up node")
	rospy.init_node('cylinder_test', anonymous=False)
	
	rospy.wait_for_service('detect_cylinder')
	try:
		get_ring_location = rospy.ServiceProxy('detect_cylinder', GetLocation)
		get_ring_location()
	except rospy.ServiceException, e:
		print "Service call failed: %s"%e



if __name__ == '__main__':
	main()

