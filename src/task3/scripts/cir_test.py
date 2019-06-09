#!/usr/bin/env python

import sys
import rospy
from task3.srv import *

def get_color_client():
    # get position
		rospy.wait_for_service('check_if_reachable')
		try:
				cir = rospy.ServiceProxy('check_if_reachable', GetColor)
				message = GetColorRequest()
				message.cam_X = 0.0
				message.cam_Y = 0.0
				message.cam_Z = 0.0
				message.map_X = float(raw_input("enter X coordinate: "))
				message.map_Y = float(raw_input("enter Y coordinate: "))
				message.map_Z = 0.0
				
				response = cir(message)
				res = response.color
				
				if(res == 1):
					print("it is reachable")
				else:
					print("it is not reachable")
		except rospy.ServiceException, e:
				print "Service call failed: %s"%e

if __name__ == "__main__":
    get_color_client()
