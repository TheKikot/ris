#!/usr/bin/env python

import sys
import rospy
from task3.srv import *
from std_msgs.msg import String

def main():
    # get image
	rospy.init_node('cylinder_test', anonymous=False)
	points_pub = rospy.Publisher("/detect_cylinder", String, queue_size=1)
	points_pub.publish("a")

if __name__ == "__main__":
    main()
    print ""
