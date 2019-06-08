#!/usr/bin/env python

import sys
import rospy
from task3.srv import *

def accu_positions():
    # get image
    rospy.wait_for_service('/return_positions')
    try:
        check_accu = rospy.ServiceProxy('/return_positions', GetPositions)
        check_accu()
    except rospy.ServiceException, e:
        print "Service call failed: %s"%e

if __name__ == "__main__":
    accu_positions()
    # print ""
