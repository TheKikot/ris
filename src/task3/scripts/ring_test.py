#!/usr/bin/env python

import sys
import rospy
from task3.srv import *

def get_location_client():
    # get image
		rospy.wait_for_service('get_ring_location')
		try:
				get_ring_location = rospy.ServiceProxy('get_ring_location', GetLocation)
				get_ring_location()
		except rospy.ServiceException, e:
				print "Service call failed: %s"%e

if __name__ == "__main__":
    get_location_client()
    print ""
