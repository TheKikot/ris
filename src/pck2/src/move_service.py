#!/usr/bin/env python

import rospy
from pck2.srv import movesrv
from geometry_msgs.msg import Twist

def rectangle_movement(step):

  twist = Twist()
  twist.linear.x = 0.1
  step = step % 20

  if step % 5 == 0:
    twist.linear.x = 0
    twist.angular.z = 1.57 #(90 / 360) * 2 * 3.14

  return twist


def move_server_function(req):
    print("Shape: " + req.shape)
    #print("TIME: " + (str)req.time)
    return "7"

def move_service():
    rospy.init_node('move_service')
    s = rospy.Service('move', movesrv, move_server_function)
    print "Ready to move."
    rospy.spin()

if __name__ == "__main__":
    move_service()
