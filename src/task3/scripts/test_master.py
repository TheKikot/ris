#!/usr/bin/python
import rospy
from task3.srv import *

rospy.init_node('master_test', anonymous=False)
rospy.wait_for_service('start_master')
masterService = rospy.ServiceProxy('start_master', GetLocation)
masterService()
