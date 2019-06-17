#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import print_function

import rospy
from geometry_msgs.msg import PointStamped, Vector3, Pose
from visualization_msgs.msg import Marker, MarkerArray
from task3.msg import *
from task3.srv import *
from sklearn.neighbors import KNeighborsClassifier
from os.path import expanduser
import math

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
			self.color = 3
		elif(red == 1.0):
			self.color = 0
		elif(green == 1.0):
			self.color = 1
		elif(blue == 1.0):
			self.color = 2


class Accumulator():


	def build_classifier(self):
		home = expanduser("~")
		f = open(home + "/ROS/barvni_podatki.txt", "r")
		text = f.read()
		lines = text.splitlines()
		self.features = []
		self.label = []

		for line in lines[1:]: # For each line except the first (this is the description line)
			#print(line)
			b, g, r, barva = [float(x) for x in line.split(',')] # x1 and x2 are inputs and y is the output
			self.features.append([b,g,r])
			self.label.append(barva)

		self.model = KNeighborsClassifier(n_neighbors = 5)
		self.model.fit(self.features, self.label)


	def get_prediction(self, b, g, r):
	    return self.model.predict([[b, g, r]])

	def __init__(self):
		rospy.init_node("accumulator")
        # Subscribe to the image and/or depth topic
		self.rings_with_normals_sub = rospy.Subscriber("/rings_with_normals", ringAndNormal, self.new_ring_and_normal)
		self.cylinder_sub = rospy.Subscriber("/cylinder_with_color", Marker, self.new_cylinder)
		self.service = rospy.Service("/return_positions", GetPositions, self.return_positions)
		self.rings = None
		self.cylinders = None
		self.build_classifier()

	def getCylColor(self, b, g, r):
		if (b == 1):
			return 2
		elif (g == 1 and r == 1):
			return 3
		elif(g == 1):
			return 1
		else:
			return 0

	def return_positions(self, gp):

		print(gp)

		x = []
		y = []
		colors = []
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
				colors.append(self.get_prediction(r.blue, r.green, r.red))
				print("Ring - X, Y, count, color")
				print(x[-1], y[-1], count[-1], colors[-1])

		cylX = []
		cylY = []
		cylCount = []
		cylColors = []

		if(not self.cylinders == None):
			for c in self.cylinders:
				cylX.append(c.x)
				cylY.append(c.y)
				cylCount.append(c.count)
				cylColors.append(c.color)
				print("Cylinder - X, Y, count, color")
				print(cylX[-1], cylY[-1], cylCount[-1], cylColors[-1])

		gpResp = GetPositionsResponse()
		gpResp.ringsX = x;
		gpResp.ringsY = y;
		gpResp.ringsColor = colors
		gpResp.ringsCount = count
		gpResp.normalsX = normalX
		gpResp.normalsY = normalY
		gpResp.cylnsX = cylX
		gpResp.cylnsY = cylY
		gpResp.cylnsColor = cylColors
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
					
					# popravim povprečje normal
					r.normalX = (r.normalX * r.count + rn.normalX) / (r.count+1)
					r.normalY = (r.normalY * r.count + rn.normalY) / (r.count+1)
										
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
		if(math.isnan(x) or math.isnan(y)):
			print('The cylinders had nans')
			return

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
