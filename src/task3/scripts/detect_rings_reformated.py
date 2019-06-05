#!/usr/bin/python
# -*- coding: utf-8 -*-

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
from task3.srv import *
import pytesseract

#--------- QR ------------

import pyzbar.pyzbar as pyzbar

dictm = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_6X6_250)

# The object that we will pass to the markerDetect function
params =  cv2.aruco.DetectorParameters_create()

print(params.adaptiveThreshConstant) 
print(params.adaptiveThreshWinSizeMax)
print(params.adaptiveThreshWinSizeMin)
print(params.minCornerDistanceRate)
print(params.adaptiveThreshWinSizeStep)

# To see description of the parameters
# https://docs.opencv.org/3.3.1/d1/dcd/structcv_1_1aruco_1_1DetectorParameters.html

# You can set these parameters to get better marker detections
#params.adaptiveThreshConstant = 25
#adaptiveThreshWinSizeStep = 2
#params.adaptiveThreshWinSizeMin = 40
#params.adaptiveThreshWinSizeMax = 60
#params.minCornerDistanceRate = 100000
#params.adaptiveThreshWinSizeStep = 10


#--------- QR --------------

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

        self.markers_pub = rospy.Publisher('rings', Marker,
                queue_size=1)

        # Object we use for transforming between coordinate frames

        self.tf_buf = tf2_ros.Buffer()
        self.tf_listener = tf2_ros.TransformListener(self.tf_buf)

        # Service

        self.service = rospy.Service('get_ring_location', GetLocation,
                self.image_callback)

    def get_pose(self, e, dist):

        # Calculate the position of the detected ellipse

        k_f = 525  # kinect focal length in pixels

        elipse_x = self.dims[1] / 2 - e[0][0]
        elipse_y = self.dims[0] / 2 - e[0][1]

        angle_to_target = np.arctan2(elipse_x, k_f)

        # Get the angles in the base_link relative coordinate system

        (x, y) = (dist * np.cos(angle_to_target), dist
                  * np.sin(angle_to_target))

        # ## Define a stamped message for transformation - directly in "base_frame"
        # point_s = PointStamped()
        # point_s.point.x = x
        # point_s.point.y = y
        # point_s.point.z = 0.3
        # point_s.header.frame_id = "base_link"
        # point_s.header.stamp = rospy.Time(0)

        # Define a stamped message for transformation - in the "camera rgb frame"

        point_s = PointStamped()
        point_s.point.x = -y
        point_s.point.y = 0
        point_s.point.z = x
        point_s.header.frame_id = 'camera_rgb_optical_frame'
        point_s.header.stamp = rospy.Time(0)

        # Get the point in the "map" coordinate system

        point_world = self.tf_buf.transform(point_s, 'map')

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

        #self.marker_array.markers.append(marker)

        #self.markers_pub.publish(self.marker_array)

    def image_callback(self, krneki):
        print('I got a new image!')
        data = rospy.wait_for_message('/camera/rgb/image_raw', Image)


        try:
            print('converting image')
            cv_image = self.bridge.imgmsg_to_cv2(data, 'bgr8')
            print('image converted!')
        except CvBridgeError, e:
            print(e)

        # 640x480

        #cv_image = cv_image[80:420, 0:640]
        cv_image_copy = cv_image.copy()

        # Set the dimensions of the image

        self.dims = cv_image.shape

        # Tranform image to gayscale

        gray = cv2.cvtColor(cv_image, cv2.COLOR_BGR2GRAY)


        # Do histogram equlization

        img = cv2.equalizeHist(gray)


        # Binarize the image
        # ret, thresh = cv2.threshold(img, 50, 255, 0)

        thresh = cv2.adaptiveThreshold(
            img,
            255,
            cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
            cv2.THRESH_BINARY,
            151,
            2,
            )

        #cv2.waitKey(0)

        kernel = np.ones((3, 3), np.uint8)

        #thresh = cv2.dilate(thresh, kernel, iterations = 1)
        #cv2.waitKey(0)

        # Extract contours

        (im2, contours, hierarchy) = cv2.findContours(thresh,
                cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

        #Example how to draw the contours
        #cv2.drawContours(img, contours, -1, (255, 0, 0), 3)

        #Fit elipses to all extracted contours

        elps = []
        ellipseContours = []
        for cnt in contours:

            #print cnt
            #print cnt.shape

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
                dist = np.sqrt((e1[0][0] - e2[0][0]) ** 2 + (e1[0][1]
                               - e2[0][1]) ** 2)
                dist2 = abs(e1[1][1] / e1[1][0] - e2[1][1] / e2[1][0])
                sizediff = abs(e1[1][1] - e2[1][1]) + abs(e1[1][0]
                        - e2[1][0])

                #print dist

                if dist < 5 and dist2 < 0.2 and sizediff < 150:
                    candidates.append((e1, e2))
                    candidates_cnt.append((ellipseContours[n],
                            ellipseContours[m]))

        print('Processing is done! found', len(candidates),
              'candidates for rings')
        if len(candidates) < 1:
            print('1')
            a = random.randrange(1000)
            cv2.imwrite('camera_image_' + str(a) + '.jpeg', cv_image)
            cv2.imwrite('camera_image_' + str(a) + '_threshed.jpeg',
                        thresh)
            return []

        # '''
        # print("2")

        try:
            depth_img = \
                rospy.wait_for_message('/camera/depth_registered/image_raw'
                    , Image)

            # depth_img = rospy.wait_for_message('/camera/depth/image_raw', Image)
            # depth_img = depth_img[0:240, 0:640]

            print('success')
        except Exception, e:
            print(e)

        # '''
        # print("3")
        # Extract the depth from the depth image

        for n in range(len(candidates)):
            e = candidates[n]
            c = candidates_cnt[n]

            # the centers of the ellipses

            e1 = e[0]
            e2 = e[1]

            # drawing the ellipses on the image

            size = (e1[1][0] + e1[1][1]) / 2
            center = (e1[0][1], e1[0][0])

            # print(4)

            x1 = int(center[0] - size / 2)
            x2 = int(center[0] + size / 2)
            x_min = (x1 if x1 > 0 else 0)
            x_max = (x2 if x2
                     < cv_image.shape[0] else cv_image.shape[0])

            # print(5)

            y1 = int(center[1] - size / 2)
            y2 = int(center[1] + size / 2)
            y_min = (y1 if y1 > 0 else 0)
            y_max = (y2 if y2
                     < cv_image.shape[1] else cv_image.shape[1])

            # print(6)

            depth_image = self.bridge.imgmsg_to_cv2(depth_img, '16UC1')

            # org size 640x480

            #depth_image = depth_image[80:420, 0:640]

            # depth_image = depth_img

            dist = depth_image[int(e1[0][1]), int(e1[0][0])]
            #print(dist)

            # self.check_if_floating(e1, c[0], e2, c[1], depth_image)

            self.get_pose(e1, dist / 1000.0)
            cv2.ellipse(cv_image, e1, (255, 0, 0), 2)
            cv2.ellipse(cv_image, e2, (255, 0, 0), 2)

            # print(7)

        if len(candidates) > 0:
            print('Found ', len(candidates), 'circles')
            a = str(random.randrange(1000))
            cv2.imwrite('circles_camera_image_' + a + '.jpeg', cv_image)
            cv2.imwrite('circles_camera_image_' + a + '_threshed.jpeg', thresh)

            # Convert the depth image to a Numpy array since most cv2 functions
            # require Numpy arrays.

            #depth_array = np.array(depth_image, dtype=np.float32)

            # Normalize the depth image to fall between 0 (black) and 1 (white)

            #cv2.normalize(depth_array, depth_array, 0, 1, cv2.NORM_MINMAX)

            # At this point you can display the result properly:
            # If you write it as it si, the result will be a image with only 0 to 1 values.
            # To actually store in a this a image like the one we are showing its needed
            # to reescale the otuput to 255 gray scale.

            #cv2.imwrite('depth_circles_image_' + a + '.png', depth_array * 255)

            corners, ids, rejected_corners = cv2.aruco.detectMarkers(cv_image_copy,dictm,parameters=params)
            
            # Increase proportionally if you want a larger image
            image_size=(351,248,3)
            marker_side=50

            img_out = np.zeros(image_size, np.uint8)
            out_pts = np.array([[marker_side/2,img_out.shape[0]-marker_side/2],
                                [img_out.shape[1]-marker_side/2,img_out.shape[0]-marker_side/2],
                                [marker_side/2,marker_side/2],
                                [img_out.shape[1]-marker_side/2,marker_side/2]])

            src_points = np.zeros((4,2))
            cens_mars = np.zeros((4,2))

            if not ids is None:
                if len(ids)==4:
                    print('4 Markers detected')
            
                    for idx in ids:
                        # Calculate the center point of all markers
                        cors = np.squeeze(corners[idx[0]-1])
                        cen_mar = np.mean(cors,axis=0)
                        cens_mars[idx[0]-1]=cen_mar
                        cen_point = np.mean(cens_mars,axis=0)
                
                    for coords in cens_mars:
                        #  Map the correct source points
                        if coords[0]<cen_point[0] and coords[1]<cen_point[1]:
                            src_points[2]=coords
                        elif coords[0]<cen_point[0] and coords[1]>cen_point[1]:
                            src_points[0]=coords
                        elif coords[0]>cen_point[0] and coords[1]<cen_point[1]:
                            src_points[3]=coords
                        else:
                            src_points[1]=coords

                    h, status = cv2.findHomography(src_points, out_pts)
                    img_out = cv2.warpPerspective(cv_image_copy, h, (img_out.shape[1],img_out.shape[0]))
                    
                    ################################################
                    #### Extraction of digits starts here
                    ################################################
                    
                    # Cut out everything but the numbers
                    
                    
                    # Convert the image to grayscale
                    img_out = cv2.cvtColor(img_out, cv2.COLOR_BGR2GRAY)
                    cv2.imwrite('img_out_pre_threshold.jpeg', img_out)
                    img_out_QR = img_out[105:241, 50:195]
                    
                    # Option 1 - use ordinairy threshold the image to get a black and white image
                    ret,img_out = cv2.threshold(img_out,100,255,0)

                    # Option 1 - use adaptive thresholding
                    #img_out = cv2.adaptiveThreshold(img_out,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,5)

                    img_out_digits = img_out[125:221,50:195]
                    
                    
                    # Use Otsu's thresholding
                    #ret,img_out = cv2.threshold(img_out,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
                    
                    # Pass some options to tesseract
                    config = '--psm 13 outputbase nobatch digits'
                    
                    # Visualize the image we are passing to Tesseract
                    cv2.imwrite('img_out_digits.jpeg', img_out_digits)
                    cv2.imwrite('img_out_QR.jpeg', img_out_QR)
                    
                    # Extract text from image
                    text = pytesseract.image_to_string(img_out_digits, config = config)
                    
                    # Check and extract data from text
                    print('Extracted>>',text)
                    
                    # Remove any whitespaces from the left and right
                    text = text.strip()
                    
      #             # If the extracted text is of the right length
                    if len(text)==2:
                        x=int(text[0])
                        y=int(text[1])
                        print('The extracted datapoints are x=%d, y=%d' % (x,y))
                    else:
                        print('The extracted text has is of length %d. Aborting processing' % len(text))
                        print("Looking for QR codes")
                        # Find a QR code in the image
                        decodedObjects = pyzbar.decode(img_out_QR)
                        cv2.imwrite('cv_image_copy.png',
                                    cv_image_copy)
                        
                        #print(decodedObjects)
                        
                        if len(decodedObjects) == 1:
                            dObject = decodedObjects[0]
                            print("Found 1 QR code in the image!")
                            print("Data: ", dObject.data,'\n')
                            
                            # Visualize the detected QR code in the image
                            points  = dObject.polygon
                            if len(points) > 4 : 
                                hull = cv2.convexHull(np.array([point for point in points], dtype=np.float32))
                                hull = list(map(tuple, np.squeeze(hull)))
                            else : 
                                hull = points;
                             
                            ## Number of points in the convex hull
                            n = len(hull)
                         
                            ## Draw the convext hull
                            for j in range(0,n):
                                cv2.line(img_out_QR, hull[j], hull[ (j+1) % n], (0,255,0), 2)
                                
                            cv2.imwrite('QR_image_.png',
                                    img_out_QR)
                                
                        elif len(decodedObjects)==0:
                            print("No QR code in the image")
                            #TODO mapa
                        else:
                            print("Found more than 1 QR code")

                    
                else:
                    print('The number of markers is not ok:',len(ids))
            else:
                 print('No markers found')

            
        else:

            print('Didnt find any circles. ')

        return []

    def depth_callback(self, data):

        try:
            depth_image = self.bridge.imgmsg_to_cv2(data, '16UC1')
        except CvBridgeError, e:
            print(e)

        # Do the necessairy conversion so we can visuzalize it in OpenCV

        image_1 = depth_image / 65536.0 * 255
        image_1 = image_1 / np.max(image_1) * 255

        image_viz = np.array(image_1, dtype=np.uint8)



def main():

    ring_finder = The_Ring()

    try:
        rospy.spin()
    except KeyboardInterrupt:
        print('Shutting down')

    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()


			