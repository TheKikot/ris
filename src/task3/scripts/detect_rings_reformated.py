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
from sklearn.neighbors import KNeighborsClassifier
import pytesseract
import urllib2
from task3.msg import *

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

    global model
    global features
    global label

    def test_recognition(self):
        self.get_online_data('http://box.vicos.si/rins/w.txt')
        global label
        #print(label)
        self.build_classifier()
        print(self.get_prediction(1,5))

    def get_online_data(self, url):
        # Then we cen get the contents
        resp = urllib2.urlopen(url)
        text = resp.read()

        # Split the text into lines
        lines = text.splitlines()

        global features
        global label

        features = []
        label = []

        # Extract the data from the text.
        # You should modify these lines so you put the extracted points into
        # whatever structure you need for the learning of the classifier.
        for line in lines[1:]: # For each line except the first (this is the description line)
            x1, x2, y = [float(x) for x in line.split(',')] # x1 and x2 are inputs and y is the output
            features.append([x1,x2])
            label.append(y)


    def build_classifier(self):
        global model, features, label
        model = KNeighborsClassifier(n_neighbors = 5)
        model.fit(features, label)
    

    def get_prediction(self, x, y):
        global model
        return model.predict([[x,y]])

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
        self.normals_pub = rospy.Publisher('normals', Marker, queue_size=1)
        self.rn_pub = rospy.Publisher('rings_with_normals', ringAndNormal, queue_size=1)

        # Object we use for transforming between coordinate frames

        self.tf_buf = tf2_ros.Buffer()
        self.tf_listener = tf2_ros.TransformListener(self.tf_buf)

        # Service

        self.service = rospy.Service('get_ring_location', GetLocation,
                self.image_callback)

    def get_pose(self, e, c1, c2, depth_image, bgr_image):
                

        
        point1X = c1[0][0][0]
        #print(point1X)
        point1Y = c1[0][0][1]
        #print(point1Y)
        point2X = c1[int(len(c1) / 4)][0][0]
        point2Y = c1[int(len(c1) / 4)][0][1]
        point3X = c1[int(len(c1) / 4) * 2][0][0]
        #print(point3X)
        point3Y = c1[int(len(c1) / 4) * 2][0][1]
        #print(point3Y)
        point4X = c1[int(len(c1) / 4) * 3][0][0]
        point4Y = c1[int(len(c1) / 4) * 3][0][1]

        min1 = 1000000000
        closest1 = c1[0]
        min2 = 1000000000
        closest2 = c1[0]
        min3 = 1000000000
        closest3 = c1[0]
        min4 = 1000000000
        closest4 = c1[0]

        for i in range(0, len(c2)) :
            dist1 = np.sqrt((c2[i][0][0]-point1X) ** 2 + (c2[i][0][1] - point1Y) ** 2)
            if dist1 < min1 :
                min1 = dist1
                closest1 = c2[i][0]

            dist2 = np.sqrt((c2[i][0][0]-point2X) ** 2 + (c2[i][0][1] - point2Y) ** 2)
            if dist2 < min2 :
                min2 = dist2
                closest2 = c2[i][0]

            dist3 = np.sqrt((c2[i][0][0]-point3X) ** 2 + (c2[i][0][1] - point3Y) ** 2)
            if dist3 < min3 :
                min3 = dist3
                closest3 = c2[i][0]

            dist4 = np.sqrt((c2[i][0][0]-point4X) ** 2 + (c2[i][0][1] - point4Y) ** 2)
            if dist4 < min4 :
                min4 = dist4
                closest4 = c2[i][0]
      
        por1X = (point1X + closest1[0])/2
        por1Y = (point1Y + closest1[1])/2

        por2X = (point2X + closest2[0])/2
        por2Y = (point2Y + closest2[1])/2

        por3X = (point3X + closest3[0])/2
        por3Y = (point3Y + closest3[1])/2

        por4X = (point4X + closest4[0])/2
        por4Y = (point4Y + closest4[1])/2

        #avgRingDepth = (depth_image[por1Y, por1X]/4 + depth_image[por2Y, por2X]/4 + depth_image[por3Y, por3X]/4 + depth_image[por4Y, por4X]/4)
        avgRingDepth = depth_image[int(e[0][1]), int(e[0][0])]
        avgRed = (bgr_image[por1Y, por1X, 2]/4 + bgr_image[por2Y, por2X, 2]/4 + bgr_image[por3Y, por3X, 2]/4 + bgr_image[por4Y, por4X, 2]/4)
        
        avgBlue = (bgr_image[por1Y, por1X, 0]/4 + bgr_image[por2Y, por2X, 0]/4 + bgr_image[por3Y, por3X, 0]/4 + bgr_image[por4Y, por4X, 0]/4)
        
        avgGreen = (bgr_image[por1Y, por1X, 1]/4 + bgr_image[por2Y, por2X, 1]/4 + bgr_image[por3Y, por3X, 1]/4 + bgr_image[por4Y, por4X, 1]/4)
         
        #print("distance, BGR", avgRingDepth, avgBlue, avgGreen, avgRed);

        # Calculate the position of the detected ellipse

        # CENTER
        k_f = 525  # kinect focal length in pixels

        elipse_x = self.dims[1] / 2 - e[0][0]
        elipse_y = self.dims[0] / 2 - e[0][1]

        angle_to_center = np.arctan2(elipse_x, k_f)

        # Get the angles in the base_link relative coordinate system

        (x_center, y_center) = (avgRingDepth/1000.0 * np.cos(angle_to_center), avgRingDepth/1000.0
                  * np.sin(angle_to_center))
        #print("x,y,center", x_center, y_center)

        size = (e[1][0]+e[1][1])/2
        center = (e[0][1], e[0][0])

        #print("image shape", bgr_image.shape)

        x1 = int(center[0] )
        x2 = int(center[0] )
        x_min = x1 if x1>0 else 0
        x_max = x2 if x2<bgr_image.shape[0] else bgr_image.shape[0]
        #print("x_min, x_max", x_min, x_max)

        y1 = int(center[1] - size / 2)
        y2 = int(center[1] + size / 2)
        y_min = y1 if y1 > 0 else 0
        y_max = y2 if y2 < bgr_image.shape[1] else bgr_image.shape[1]
        #print("y_min, y_max", y_min, y_max)

        # Draw a diagonal blue line with thickness of 5 px
        #cv2.line(bgr_image,(y_min,x_min),(y_max,x_max),(255,0,0),5)
        #cv2.imwrite('debug.jpeg', bgr_image)

        # Convert the depth image to a Numpy array since most cv2 functions
        # require Numpy arrays.

        #depth_array = np.array(depth_image, dtype=np.float32)

        # Normalize the depth image to fall between 0 (black) and 1 (white)

        #cv2.normalize(depth_array, depth_array, 0, 1, cv2.NORM_MINMAX)

        # At this point you can display the result properly:
        # If you write it as it si, the result will be a image with only 0 to 1 values.
        # To actually store in a this a image like the one we are showing its needed
        # to reescale the otuput to 255 gray scale.

        #cv2.imwrite('debug_depth.png', depth_array * 255)

        
        # POINT 1

        elipse_x = self.dims[1] / 2 - y_min #morde sta zamenjana x in y
        elipse_y = self.dims[0] / 2 - x_min
        angle_to_point1 = np.arctan2(elipse_x, k_f)
        (x_1, y_1) = (depth_image[x_min, y_min]/1000.0 * np.cos(angle_to_point1), depth_image[x_min, y_min]/1000.0
                  * np.sin(angle_to_point1))

        # POINT 2

        elipse_x = self.dims[1] / 2 - y_max #morde sta zamenjana x in y
        elipse_y = self.dims[0] / 2 - x_max
        angle_to_point2 = np.arctan2(elipse_x, k_f)
        (x_2, y_2) = (depth_image[x_max, y_max]/1000.0 * np.cos(angle_to_point2), depth_image[x_max, y_max]/1000.0
                  * np.sin(angle_to_point2))

        #print("koti", angle_to_center, angle_to_point1, angle_to_point2)
        #print("x1, y1, x2, y2 pred transformom", x_1, y_1, x_2, y_2)

        #print("avgDepth, depth_levo, depth_desno", avgRingDepth, depth_image[x_min, y_min], depth_image[x_max, y_max])
        
        point_s = PointStamped()
        point_s.point.x = -y_center
        point_s.point.y = 0
        point_s.point.z = x_center
        point_s.header.frame_id = 'camera_rgb_optical_frame'
        point_s.header.stamp = rospy.Time(0)

        # Get the point in the "map" coordinate system

        point_world = self.tf_buf.transform(point_s, 'map')
        #print("center", point_world.point.x, point_world.point.y)

        # Create a Pose object with the same position

        pose = Pose()
        pose.position.x = point_world.point.x
        pose.position.y = point_world.point.y
        pose.position.z = point_world.point.z

        # POINT 1

        point_s1 = PointStamped()
        point_s1.point.x = -y_1
        point_s1.point.y = 0
        point_s1.point.z = x_1
        point_s1.header.frame_id = 'camera_rgb_optical_frame'
        point_s1.header.stamp = rospy.Time(0)

        # Get the point in the "map" coordinate system

        point_world1 = self.tf_buf.transform(point_s1, 'map')

        x_1 = point_world1.point.x
        y_1 = point_world1.point.y

        # POINT 2

        point_s2 = PointStamped()
        point_s2.point.x = -y_2
        point_s2.point.y = 0
        point_s2.point.z = x_2
        point_s2.header.frame_id = 'camera_rgb_optical_frame'
        point_s2.header.stamp = rospy.Time(0)

        # Get the point in the "map" coordinate system

        point_world2 = self.tf_buf.transform(point_s2, 'map')

        x_2 = point_world2.point.x
        y_2 = point_world2.point.y

        
        # Marker for circle
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


        # CALCULATING NORMAL
        # {x,y} -> {y,-x}
        #print("x1, y1, x2, y2", x_1, y_1, x_2, y_2)
        #xy = [x_1-x_2, y_1-y_2]
        #print(xy)
        normala = [y_1-y_2, -(x_1-x_2)]
        #print("normala", normala)
        normala[0] = normala[0] / ((normala[0]**2+normala[1]**2)**(1/2))
        normala[1] = normala[1] / ((normala[0]**2+normala[1]**2)**(1/2))
        #print("normalizirana normala", normala)

        pose3 = Pose()
        pose3.position.x = point_world.point.x + normala[0]
        pose3.position.y = point_world.point.y + normala[1]
        pose3.position.z = point_world.point.z

        # Marker for point perpendicular
        self.marker_num += 1
        marker = Marker()
        marker.header.stamp = point_world.header.stamp
        marker.header.frame_id = point_world.header.frame_id
        marker.pose = pose3
        marker.type = Marker.CUBE
        marker.action = Marker.ADD
        marker.frame_locked = False
        marker.lifetime = rospy.Duration.from_sec(10)
        marker.id = self.marker_num
        marker.scale = Vector3(0.1, 0.1, 0.1)
        marker.color = ColorRGBA(1, 1, 1, 1)
        self.normals_pub.publish(marker)

        ringNormal = ringAndNormal()
        ringNormal.ringX = point_world.point.x
        ringNormal.ringY = point_world.point.y
        ringNormal.normalX = point_world.point.x + normala[0]
        ringNormal.normalY = point_world.point.y + normala[1]
        ringNormal.red = avgRed;
        ringNormal.blue = avgBlue;
        ringNormal.green = abgGreen;
        self.rn_pub.publish(ringNormal)

        return(avgRingDepth/1000)

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

        thresh = cv2.dilate(thresh, kernel, iterations = 1)
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
        print()
        if len(candidates) < 1:
            #print('1')
            #a = random.randrange(1000)
            #cv2.imwrite('camera_image_' + str(a) + '.jpeg', cv_image)
            #cv2.imwrite('camera_image_' + str(a) + '_threshed.jpeg',
            #            thresh)
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

            #dist = depth_image[int(e1[0][1]), int(e1[0][0])]
            #print(dist)

            # self.check_if_floating(e1, c[0], e2, c[1], depth_image)

            #self.get_pose(e1, dist / 1000.0)

            distance = self.get_pose(e1, c[0], c[1], depth_image, cv_image_copy)

            cv2.ellipse(cv_image, e1, (255, 0, 0), 2)
            cv2.ellipse(cv_image, e2, (255, 0, 0), 2)

            # print(7)

        if len(candidates) > 0 and distance < 2.0:
            print('Found ', len(candidates), 'circles')
            a = str(random.randrange(1000))
            #cv2.imwrite('circles_camera_image_' + a + '.jpeg', cv_image)
            #cv2.imwrite('circles_camera_image_' + a + '_threshed.jpeg', thresh)

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


            #----------------------------------
            #----------CIFRE-------------------
            #----------------------------------
            '''
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
                    #cv2.imwrite('img_out_pre_threshold.jpeg', img_out)
                    #img_out_QR = img_out[105:241, 50:195]
                    
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
                    #cv2.imwrite('img_out_digits.jpeg', img_out_digits)
                    #cv2.imwrite('img_out_QR.jpeg', img_out_QR)
                    
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
                        return []
                    else:
                        print('The extracted text has is of length %d. Aborting processing' % len(text))
                    
                else:
                    print('The number of markers is not ok:',len(ids))
            else:
                 print('No markers found')

            #----------------------------------
            #----------CIFRE-------------------
            #----------------------------------
            '''

            #----------------------------------
            #----------QR----------------------
            #----------------------------------
            '''
            print()
            print('Looking for qrCodes')
            for i in range(0, 5):
                qr_data = self.check_for_QR()
                if(qr_data != 0):
                    break;

            if(qr_data == 0):
                print('No qr codes found')
            else:
                print("QR data:", qr_data)            
            '''
            
        else:

            print('Didnt find any circles. ')

        return []

'''
    def check_for_QR(self):
        
        data = rospy.wait_for_message('/camera/rgb/image_raw', Image)
        print('Grabbed a new image')


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

        kernel = np.ones((3, 3), np.uint8)

        #thresh = cv2.dilate(thresh, kernel, iterations = 1)
        #cv2.waitKey(0)


        
        print("Looking for QR codes")
        # Find a QR code in the image
        decodedObjects = pyzbar.decode(thresh)
        cv2.imwrite('cv_image_copy.png',
                    cv_image_copy)
        
        #print(decodedObjects)
        
        if len(decodedObjects) == 1:
            dObject = decodedObjects[0]
            print("Found 1 QR code in the image!")
            print("Data: ", dObject.data,'\n')
            return dObject.data;        

                
        elif len(decodedObjects)==0:
            print("Havent found any QR codes")
            return 0;
            #TODO mapa
        else:
            print("Found more than 1 QR code")
            return 0;
'''



def main():

    ring_finder = The_Ring()
    #ring_finder.test_recognition()

    try:
        rospy.spin()
    except KeyboardInterrupt:
        print('Shutting down')

    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()


			