#!/usr/bin/env python

import rospy
#import python-pcl
from sensor_msgs.msg import PointCloud2
import sensor_msgs.point_cloud2 as pc2

def call_detection(points):
	print("klicem funkcijo")
	points_pub = rospy.Publisher("input", PointCloud2, queue_size=1)
	points_pub.publish(points)	
	rospy.sleep(1)





def main():
	print("setting up node")
	rospy.init_node('cylinder_detection', anonymous=False)
	
	points_sub = rospy.Subscriber("/camera/depth_registered/points", PointCloud2, call_detection)

	try:
		rospy.spin()
	except KeyboardInterrupt:
	  print("Shutting down")



if __name__ == '__main__':
	main()
