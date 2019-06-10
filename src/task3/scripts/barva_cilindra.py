#!/usr/bin/python
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
import glob2 as glob
from scipy.spatial import distance as dist

class Comparer:
    def __init__(self):

        # initialize the index dictionary to store the image name
        # and corresponding histograms and the images dictionary
        # to store the images themselves
        self.index = {}
        self.images = {}

        # loop over the image paths
        for imagePath in glob.glob("/home/mihael/ROS/images/*.jpeg"):
            print(imagePath)
            # extract the image filename (assumed to be unique) and
            # load the image, updating the images dictionary
            filename = imagePath[imagePath.rfind("/") + 1:]
            image = cv2.imread(imagePath)
            self.images[filename] = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

            # extract a 3D RGB color histogram from the image,
            # using 8 bins per channel, normalize, and update
            # the index
            hist = cv2.calcHist([image], [0, 1, 2], None, [8, 8, 8],
                                [0, 256, 0, 256, 0, 256])
            hist = cv2.normalize(hist, hist).flatten()
            self.index[filename] = hist

    def compare(self, image):
        cv_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        newHist = cv2.calcHist([image], [0, 1, 2], None, [8, 8, 8],
                                [0, 256, 0, 256, 0, 256])
        newHist = cv2.normalize(newHist, newHist).flatten()

        minD = 1000000000000
        name = ""
        for (key, hist) in self.index.items():
            # compute the distance between the two histograms
            # using the method and update the results dictionary
            d = cv2.compareHist(newHist, hist, cv2.HISTCMP_BHATTACHARYYA)
            if(d < minD):
                minD = d
                name = key
        print("name: ", name, "minD", minD)
    	return name, minD


global comparer

def color_handler(location):
	
	#print('I got a new image!')
	data = rospy.wait_for_message('/camera/rgb/image_raw', Image)
	try:
		#print('converting image')
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
	name, minD = comparer.compare(crop)
	cv2.imwrite('image.jpeg', cv_image)
	cv2.imwrite(str(minD)+'.jpeg', crop)
	
	# prepoznamo barvo
	
	return 0


def main():
	rospy.init_node('cylinder_color', anonymous=False)
	call_srv = rospy.Service('cylinder_color', GetColor, color_handler)

	global comparer
	comparer = Comparer()
	
	try:
		rospy.spin()
	except KeyboardInterrupt:
	  print("Shutting down")



if __name__ == '__main__':
	main()
	
