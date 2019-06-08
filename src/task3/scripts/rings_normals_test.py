#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import print_function

import rospy
from geometry_msgs.msg import PointStamped, Vector3, Pose
from visualization_msgs.msg import Marker, MarkerArray
from task3.msg import *

class Test():

	def __init__(self):
		rospy.init_node('rings_normals_test', anonymous=False)
		rn_pub = rospy.Publisher('abc', ringAndNormal, queue_size=1)

		rn = ringAndNormal()
		rn.ringX = 33.3
		rn.ringY = 33.6
		rn.normalX = 33.8
		rn.normalY = 11.2
		print(rn)
		print(rn_pub.publish(rn))
		print("published on rings_with_normals")






def main():

	ring_finder = Test()
    #ring_finder.test_recognition()

	try:
		rospy.spin()
	except KeyboardInterrupt:
		print('Shutting down')



if __name__ == '__main__':
	main()
