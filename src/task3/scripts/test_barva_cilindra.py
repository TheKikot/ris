#!/usr/bin/env python

import sys
import rospy
from task3.srv import *

def get_color_client():
    # get position
		rospy.wait_for_service('cylinder_color')
		try:
				get_cyl_color = rospy.ServiceProxy('cylinder_color', GetColor)
				message = GetColorRequest()
				message.cam_X = 1.0
				message.cam_Y = 2.0
				message.cam_Z = 0.2
				message.map_X = 0.1
				message.map_Y = 0.2
				message.map_Z = 0.2
				get_cyl_color(message)
		except rospy.ServiceException, e:
				print "Service call failed: %s"%e

if __name__ == "__main__":
    get_color_client()
