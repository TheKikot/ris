#!/usr/bin/env python

import sys
import rospy
from task3.srv import *

def check_for_QR():
    # get image
		rospy.wait_for_service('check_qr')
		try:
				check_if_QR = rospy.ServiceProxy('check_qr', CheckQr)
				check_if_QR()
		except rospy.ServiceException, e:
				print "Service call failed: %s"%e

if __name__ == "__main__":
    check_for_QR()
    # print ""
