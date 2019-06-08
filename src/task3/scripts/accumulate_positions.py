#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import print_function

import rospy
from geometry_msgs.msg import PointStamped, Vector3, Pose
from visualization_msgs.msg import Marker, MarkerArray
from task3.msg import *

class Ring():

	x = 0
	y = 0
	count = 1
	normalX = 0
	normalY = 0

	def __init__(self, x, y, normalX, normalY):
		self.x = x
		self.y = y
		self.normalX = normalX
		self.normalY = normalY



class Accumulator():

	def __init__(self):
		rospy.init_node("accumulator")
        # Subscribe to the image and/or depth topic
		self.rings_with_normals_sub = rospy.Subscriber("/rings_with_normals", ringAndNormal, self.new_ring_and_normal)
		self.rings = None
		self.normals = []
		self.cylinders = []


	def sqr_distance(self, x1, y1, x2, y2):
		return ((abs(x1)-abs(x2))**2 + (abs(y1)-abs(y2))**2)

	def new_ring_and_normal(self, rn):
		print('Recieved a new ring, looking for matches')
		if(not self.rings == None):
			for r in self.rings:
				if self.sqr_distance(r.x, r.y, rn.ringX, rn.ringY) < 0.30:
					r.count += 1
					print('Found a match')
					break
			else:
				self.rings.append(Ring(rn.ringX, rn.ringY, rn.normalX, rn.normalY))
				print('Couldn\'t find a match, creating a new insesrtion on x:', rn.ringX, 'y:', rn.ringY)
		else:
			self.rings = [Ring(rn.ringX, rn.ringY, rn.normalX, rn.normalY)]


def main():

	ring_finder = Accumulator()
    #ring_finder.test_recognition()

	try:
		rospy.spin()
	except KeyboardInterrupt:
		print('Shutting down')



if __name__ == '__main__':
	main()
