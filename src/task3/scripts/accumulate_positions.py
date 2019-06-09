#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import print_function

import rospy
from geometry_msgs.msg import PointStamped, Vector3, Pose
from visualization_msgs.msg import Marker, MarkerArray
from task3.msg import *
from task3.srv import *

class Ring():

	x = 0
	y = 0
	count = 1
	normalX = 0
	normalY = 0
	red = 0
	green = 0
	blue = 0

	def __init__(self, x, y, normalX, normalY, red, green, blue):
		self.x = x
		self.y = y
		self.normalX = normalX
		self.normalY = normalY
		self.red = red
		self.green = green
		self.blue = blue

class Cylinder():

	x = 0
	y = 0
	count = 1
	color = -1

	def __init__(self, x, y, red, green, blue):
		self.x = x
		self.y = y
		if(red == 1.0 and green == 1.0):
			color = 3
		elif(red == 1.0):
			color = 0
		elif(green == 1.0):
			color = 1
		elif(blue == 1.0):
			color = 2


class Accumulator():

	def __init__(self):
		rospy.init_node("accumulator")
        # Subscribe to the image and/or depth topic
		self.rings_with_normals_sub = rospy.Subscriber("/rings_with_normals", ringAndNormal, self.new_ring_and_normal)
		self.cylinder_sub = rospy.Subscriber("/cylinder_with_color", Marker, self.new_cylinder)
		self.service = rospy.Service("/return_positions", GetPositions, self.return_positions)
		self.rings = None
		self.cylinders = None

	def return_positions(self, gp):

		print(gp)

		x = []
		y = []
		count = []
		normalX = []
		normalY = []
		if(not self.rings == None):
			for r in self.rings:
				x.append(r.x)
				y.append(r.y)
				count.append(r.count)
				normalX.append(r.normalX)
				normalY.append(r.normalY)

		cylX = []
		cylY = []
		cylCount = []

		if(not self.cylinders == None):
			for c in self.cylinders:
				cylX.append(c.x)
				cylY.append(c.y)
				cylCount.append(c.count)

		gpResp = GetPositionsResponse()
		gpResp.ringsX = x;
		gpResp.ringsY = y;
		gpResp.ringsCount = count
		gpResp.normalsX = normalX
		gpResp.normalsY = normalY
		gpResp.cylnsX = cylX
		gpResp.cylnsY = cylY
		gpResp.cylnsCount = cylCount

		return gpResp





	def sqr_distance(self, x1, y1, x2, y2):
		return ((x1 - x2)**2 + (y1 - y2)**2)

	def new_ring_and_normal(self, rn):
		print('Recieved a new ring, looking for matches')
		if(not self.rings == None):
			for r in self.rings:
				if self.sqr_distance(r.x, r.y, rn.ringX, rn.ringY) < 0.30:
					# popravim barvno povprecje
					r.red = (r.red * r.count + rn.red) / (r.count+1)
					r.blue = (r.blue * r.count + rn.blue) / (r.count+1)
					r.green = (r.green * r.count + rn.green) / (r.count+1)
					r.count += 1
					print('Found a match')
					break
			else:
				self.rings.append(Ring(rn.ringX, rn.ringY, rn.normalX, rn.normalY, rn.red, rn.green, rn.blue))
				print('Couldn\'t find a match, creating a new insesrtion on x:', rn.ringX, 'y:', rn.ringY)
		else:
			self.rings = [Ring(rn.ringX, rn.ringY, rn.normalX, rn.normalY, rn.red, rn.green, rn.blue)]

	def new_cylinder(self, marker):
		print('Recieved a new cylinder, looking for matches')
		if(not self.cylinders == None):
			for c in self.cylinders:
				if self.sqr_distance(c.x, c.y, marker.pose.position.x, marker.pose.position.y) < 0.30:
					c.count += 1
					print('Found a match')
					break
			else:
				self.cylinders.append(Cylinder(marker.pose.position.x, marker.pose.position.y, marker.color.r, marker.color.g, marker.color.b))
				print('Couldn\'t find a match, creating a new insesrtion on x:', marker.pose.position.x, 'y:', marker.pose.position.y)
		else:
			self.cylinders = [Cylinder(marker.pose.position.x, marker.pose.position.y, marker.color.r, marker.color.g, marker.color.b)]



def main():

	ring_finder = Accumulator()
    #ring_finder.test_recognition()

	try:
		rospy.spin()
	except KeyboardInterrupt:
		print('Shutting down')



if __name__ == '__main__':
	main()
