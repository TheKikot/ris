#!/usr/bin/env python
from __future__ import print_function

import random
import sys
import rospy
import cv2
import numpy as np
import tf2_geometry_msgs
import tf2_ros
from sensor_msgs.msg import Image
from geometry_msgs.msg import PointStamped, Vector3, Pose
from cv_bridge import CvBridge, CvBridgeError
from visualization_msgs.msg import Marker, MarkerArray
from std_msgs.msg import ColorRGBA
from task1.srv import *

class The_Ring:

    
    def __init__(self):
        rospy.init_node('image_converter', anonymous=True)

        # An object we use for converting images between ROS format and OpenCV format
        self.bridge = CvBridge()

        # A help variable for holding the dimensions of the image
        self.dims = (0, 0, 0)

        # Marker array object used for visualizations
        self.marker_array = MarkerArray()
        self.marker_num = 1

        # Subscribe to the image and/or depth topic
        # self.image_sub = rospy.Subscriber("/camera/rgb/image_raw", Image, self.image_callback)
        # self.depth_sub = rospy.Subscriber("/camera/depth_registered/image_raw", Image, self.depth_callback)
        
        

        # Publiser for the visualization markers
        self.markers_pub = rospy.Publisher('markers', Marker, queue_size=1)

        # Object we use for transforming between coordinate frames
        self.tf_buf = tf2_ros.Buffer()
        self.tf_listener = tf2_ros.TransformListener(self.tf_buf)
	
				# Service
	self.service = rospy.Service('get_ring_location', GetLocation, self.image_callback)

    def get_pose(self,e,dist):
        # Calculate the position of the detected ellipse

        k_f = 525 # kinect focal length in pixels

        elipse_x = self.dims[1] / 2 - e[0][0]
        elipse_y = self.dims[0] / 2 - e[0][1]

        angle_to_target = np.arctan2(elipse_x,k_f)

        # Get the angles in the base_link relative coordinate system
        x,y = dist*np.cos(angle_to_target), dist*np.sin(angle_to_target)

        ### Define a stamped message for transformation - directly in "base_frame"
        #point_s = PointStamped()
        #point_s.point.x = x
        #point_s.point.y = y
        #point_s.point.z = 0.3
        #point_s.header.frame_id = "base_link"
        #point_s.header.stamp = rospy.Time(0)

	# Define a stamped message for transformation - in the "camera rgb frame"
	point_s = PointStamped()
        point_s.point.x = -y
        point_s.point.y = 0
        point_s.point.z = x
        point_s.header.frame_id = "camera_rgb_optical_frame"
        point_s.header.stamp = rospy.Time(0)

        # Get the point in the "map" coordinate system
        point_world = self.tf_buf.transform(point_s, "map")

        # Create a Pose object with the same position
        pose = Pose()
        pose.position.x = point_world.point.x
        pose.position.y = point_world.point.y
        pose.position.z = point_world.point.z

        # Create a marker used for visualization
        self.marker_num += 1
        marker = Marker()
        marker.header.stamp = point_world.header.stamp
        marker.header.frame_id = point_world.header.frame_id
        marker.pose = pose
        marker.type = Marker.CUBE
        marker.action = Marker.ADD
        marker.frame_locked = False
        marker.lifetime = rospy.Duration.from_sec(10)
        marker.id = self.marker_num
        marker.scale = Vector3(0.1, 0.1, 0.1)
        marker.color = ColorRGBA(0, 1, 0, 1)
        self.markers_pub.publish(marker)
#        self.marker_array.markers.append(marker)

 #       self.markers_pub.publish(self.marker_array)


    def image_callback(self,krneki):
    	print('I got a new image!')
	data = rospy.wait_for_message('/camera/rgb/image_raw', Image)

	#cv2.imshow("Image window1",data)

        try:
            print('converting image')
            cv_image = self.bridge.imgmsg_to_cv2(data, "bgr8")
            print('image converted!')
        except CvBridgeError as e:
            print(e)
        
        #640x480
        cv_image = cv_image[180:380, 0:640]
            
        #cv2.imshow("Image window2",cv_image)

        # Set the dimensions of the image
        self.dims = cv_image.shape

        # Tranform image to gayscale
        gray = cv2.cvtColor(cv_image, cv2.COLOR_BGR2GRAY)
        #cv2.imshow("Image window3",gray)

        # Do histogram equlization
        img = cv2.equalizeHist(gray)
        #cv2.imshow("Image window",img)

        # Binarize the image
        #ret, thresh = cv2.threshold(img, 50, 255, 0)
	thresh = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 151,2)
	#cv2.imshow("Image window",gray)
	#cv2.imshow("Image window2",thresh)
	#cv2.waitKey(0)
	kernel = np.ones((3,3), np.uint8)
	#thresh = cv2.dilate(thresh, kernel, iterations = 1)
	#cv2.imshow("Image window3", thresh)
	#cv2.waitKey(0)
	
	
        # Extract contours
        im2, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

        # Example how to draw the contours
        # cv2.drawContours(img, contours, -1, (255, 0, 0), 3)

        # Fit elipses to all extracted contours
        elps = []
        ellipseContours = []
        for cnt in contours:
            #     print cnt
            #     print cnt.shape
            if cnt.shape[0] >= 20:
                ellipse = cv2.fitEllipse(cnt)
                elps.append(ellipse)
                ellipseContours.append(cnt)


        # Find two elipses with same centers
        candidates = []
        candidates_cnt = []
        for n in range(len(elps)):
            for m in range(n + 1, len(elps)):
                e1 = elps[n]
                e2 = elps[m]
                dist = np.sqrt(((e1[0][0] - e2[0][0]) ** 2 + (e1[0][1] - e2[0][1]) ** 2))
                dist2 = abs(e1[1][1]/e1[1][0] - e2[1][1]/e2[1][0])
                sizediff = abs(e1[1][1] - e2[1][1]) + abs(e1[1][0] - e2[1][0])
                #             print dist
                if dist < 5 and dist2 < 0.2 and sizediff < 150:
                    candidates.append((e1,e2))
                    candidates_cnt.append((ellipseContours[n], ellipseContours[m]))

	print("Processing is done! found", len(candidates), "candidates for rings")
	if len(candidates) < 1:
		print("1")
		a = random.randrange(1000)
		cv2.imwrite('camera_image_'+ str(a) + '.jpeg', cv_image)
		cv2.imwrite('camera_image_'+ str(a) + '_threshed.jpeg', thresh)
		return []
		
		#'''
        #print("2")
        try:
            depth_img = rospy.wait_for_message('/camera/depth_registered/image_raw', Image)
            #depth_img = rospy.wait_for_message('/camera/depth/image_raw', Image)
            #depth_img = depth_img[0:240, 0:640]
            print("success")
        except Exception as e:
            print(e)
		#'''
        #print("3")
        # Extract the depth from the depth image
        for n in range(len(candidates)) :
            e = candidates[n]
            c = candidates_cnt[n]
	    # the centers of the ellipses
            e1 = e[0]
            e2 = e[1]

	    # drawing the ellipses on the image
            

            size = (e1[1][0]+e1[1][1])/2
            center = (e1[0][1], e1[0][0])
            #print(4)
            x1 = int(center[0] - size / 2)
            x2 = int(center[0] + size / 2)
            x_min = x1 if x1>0 else 0
            x_max = x2 if x2<cv_image.shape[0] else cv_image.shape[0]
            #print(5)
            y1 = int(center[1] - size / 2)
            y2 = int(center[1] + size / 2)
            y_min = y1 if y1 > 0 else 0
            y_max = y2 if y2 < cv_image.shape[1] else cv_image.shape[1]

            #print(6)

            depth_image = self.bridge.imgmsg_to_cv2(depth_img, "16UC1")
            #org size 640x480
            depth_image = depth_image[180:380, 0:640]
            #depth_image = depth_img

						
            dist = depth_image[int(e1[0][1]), int(e1[0][0])]
            print(dist)
            #self.check_if_floating(e1, c[0], e2, c[1], depth_image)
            self.get_pose(e1, dist/1000.0)
            cv2.ellipse(cv_image, e1, (255, 0, 0), 2)
            cv2.ellipse(cv_image, e2, (255, 0, 0), 2)

            #print(7)

            

	if len(candidates)>0:
		print("neki")
		a = str(random.randrange(1000))
		cv2.imwrite('circles_camera_image_'+ a + '.jpeg', cv_image)
		cv2.imwrite('circles_camera_image_'+ a + '_threshed.jpeg', thresh)
		
		# Convert the depth image to a Numpy array since most cv2 functions
		# require Numpy arrays.
		depth_array = np.array(depth_image, dtype=np.float32)
		# Normalize the depth image to fall between 0 (black) and 1 (white)
		cv2.normalize(depth_array, depth_array, 0, 1, cv2.NORM_MINMAX)
		# At this point you can display the result properly:
		# cv2.imshow('Depth Image', depth_display_image)
		# If you write it as it si, the result will be a image with only 0 to 1 values.
		# To actually store in a this a image like the one we are showing its needed
		# to reescale the otuput to 255 gray scale.
		cv2.imwrite('depth_circles_image_'+ a + '.png',depth_array*255)
		
		#cv2.imshow("Image window",cv_image)
		#cv2.waitKey(0)
	else:
		print("neki2")
	
	return []
	
    

    def depth_callback(self,data):

        try:
            depth_image = self.bridge.imgmsg_to_cv2(data, "16UC1")
        except CvBridgeError as e:
            print(e)

        # Do the necessairy conversion so we can visuzalize it in OpenCV
        image_1 = depth_image / 65536.0 * 255
        image_1 =image_1/np.max(image_1)*255

        image_viz = np.array(image_1, dtype= np.uint8)

        cv2.imshow("Depth window", image_viz)
        cv2.waitKey(1)


def main():

    ring_finder = The_Ring()

    try:
        rospy.spin()
    except KeyboardInterrupt:
        print("Shutting down")

    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
