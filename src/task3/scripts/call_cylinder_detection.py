#!/usr/bin/env python

import rospy
#import python-pcl
from sensor_msgs.msg import PointCloud2
import sensor_msgs.point_cloud2 as pc2
from task3.srv import *
from std_msgs.msg import String

callFunction = False

def change_global_variable(g):
	global callFunction
	callFunction = True
	print("omogocam zaznavo valjev")
	return []

def call_detection(points):
	global callFunction
	if(callFunction):
		print("klicem funkcijo")
		points_pub = rospy.Publisher("input", PointCloud2, queue_size=1)
		points_pub.publish(points)
		callFunction = False
	else:
		rospy.sleep(1)



def main():
	print("setting up node")
	rospy.init_node('cylinder_detection', anonymous=False)
	
	points_sub = rospy.Subscriber("/camera/depth_registered/points", PointCloud2, call_detection)
	call_srv = rospy.Service('detect_cylinder', GetLocation, change_global_variable)

	try:
		rospy.spin()
	except KeyboardInterrupt:
	  print("Shutting down")



if __name__ == '__main__':
	main()
