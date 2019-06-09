#!/usr/bin/env python
from __future__ import print_function

import random
import sys
import rospy
import cv2
import math
import numpy as np
import tf2_geometry_msgs
import tf2_ros
from sensor_msgs.msg import Image
from geometry_msgs.msg import PointStamped, Vector3, Pose
from cv_bridge import CvBridge, CvBridgeError
from visualization_msgs.msg import Marker, MarkerArray
from std_msgs.msg import ColorRGBA
from task3.srv import *




def color_handler(location):
	
	#print('I got a new image!')
	data = rospy.wait_for_message('/camera/rgb/image_raw', Image)
	try:
		print('converting image')
		cv_image = CvBridge().imgmsg_to_cv2(data, 'bgr8')
		print('image converted!')
	except CvBridgeError, e:
		print(e)
	
	print(location)
	# poiscemo cilinder na sliki
	
	kot = math.degrees(math.atan2(location.cam_X,location.cam_Z))
#	kot = math.atan(location.cam_X/location.cam_Y)
#	kot = np.arcsin(location.cam_X/location.cam_Z))
#	print(kot)
#	kot = math.degrees(kot)
#	print(kot)
	print("kot: ", kot, "x: ", location.cam_X, "Y: ", location.cam_Y, "Z: ", location.cam_Z)
	print("kot: ", kot, "x: ", location.map_X, "Y: ", location.map_Y, "Z: ", location.map_Z)
	
	# 640x480
	odmik = 320.0 + (525.0/45.0) * kot
	print("odmik: ", odmik)
	
	crop = cv_image[240:250, (int(odmik)-10):(int(odmik)+10)]
	cv2.imwrite('image.jpeg', cv_image)
	cv2.imwrite('crop.jpeg', crop)
	
	# prepoznamo barvo
	
	return 0


def main():
	rospy.init_node('cylinder_color', anonymous=False)
	call_srv = rospy.Service('cylinder_color', GetColor, color_handler)
	
	try:
		rospy.spin()
	except KeyboardInterrupt:
	  print("Shutting down")



if __name__ == '__main__':
	main()
	
