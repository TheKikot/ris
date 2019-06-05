#!/usr/bin/env python

import rospy
#import python-pcl
from sensor_msgs.msg import PointCloud2
import sensor_msgs.point_cloud2 as pc2

def call_detection(points):
	points_pub = rospy.Publisher("input", PointCloud2, queue_size=1)
	print("publishing points")
	points_pub.publish(points)	





def main():
	print("running cylinder test")
	rospy.init_node('cylinder_detection', anonymous=False)
	
	points_sub = rospy.Subscriber("/camera/depth_registered/points", PointCloud2, call_detection)
	print("Shutting down")



if __name__ == '__main__':
	main()
