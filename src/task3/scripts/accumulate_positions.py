#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import print_function

import rospy
from geometry_msgs.msg import PointStamped, Vector3, Pose
from visualization_msgs.msg import Marker, MarkerArray

class Accumulator():
	def __init__(self):
		rospy.init_node("accumulator")
        # Subscribe to the image and/or depth topic
		self.ring_sub = rospy.Subscriber("/rings", Marker, self.new_ring_marker)
		self.normals_sub = rospy.Subscriber("/normals", Marker, self.new_ring_normal)

	def new_ring_marker(self, marker):
		print(marker)

	def new_ring_normal(self, marker):
		print(marker)

def main():

	ring_finder = Accumulator()
    #ring_finder.test_recognition()

	try:
		rospy.spin()
	except KeyboardInterrupt:
		print('Shutting down')



if __name__ == '__main__':
	main()
