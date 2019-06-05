#!/usr/bin/env python
<<<<<<< HEAD
#ni nč trenutno
import sys
import rospy
from task3.srv import *

def get_location_client():
    # get image
		rospy.wait_for_service('get_ring_location')
		try:
				get_cylinder_location = rospy.ServiceProxy('get_cylinder_location', GetLocation)
				get_cylinder_location()
		except rospy.ServiceException, e:
				print "Service call failed: %s"%e

if __name__ == "__main__":
    get_location_client()
    print ""
=======

import rospy
import sys
#import python-pcl
from sensor_msgs.msg import PointCloud2
import sensor_msgs.point_cloud2 as pc2

def call_detection(points):
	print("klicem funkcijo")
	points_pub = rospy.Publisher("input", PointCloud2, queue_size=1)
	points_pub.publish(points)	
	sys.exit()





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
>>>>>>> 9f88991baa5a9579ba8baed514f0109d58c703e7


