#!/usr/bin/env python

import sys
import rospy
from pck2.srv import movesrv

def move_client(shape, time):
    rospy.wait_for_service('move')
    try:
        move = rospy.ServiceProxy('move', movesrv)
        resp1 = move(shape, time)
        return 0
    except rospy.ServiceException, e:
        print "Service call failed: %s"%e


if __name__ == "__main__":
    if len(sys.argv) == 3:
        shape = sys.argv[1]
        time = int(sys.argv[2])

    move_client(shape, time)
