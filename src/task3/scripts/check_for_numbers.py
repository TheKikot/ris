#!/usr/bin/python
# -*- coding: utf-8 -*-
from task3.srv import *
import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
from std_msgs.msg import ColorRGBA
import cv2
import numpy as np
import pyzbar.pyzbar as pyzbar
import pytesseract


global bridge, dictm, params

dictm = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_6X6_250)

# The object that we will pass to the markerDetect function
params =  cv2.aruco.DetectorParameters_create()

print(params.adaptiveThreshConstant) 
print(params.adaptiveThreshWinSizeMax)
print(params.adaptiveThreshWinSizeMin)
print(params.minCornerDistanceRate)
print(params.adaptiveThreshWinSizeStep)

def main():
    print("setting up node")
    rospy.init_node('check_for_numbers', anonymous=False)
    global bridge
    bridge = CvBridge()

    call_srv = rospy.Service('check_numbers', CheckNumbers, check_for_numbers)

    try:
        rospy.spin()
    except KeyboardInterrupt:
        print("Shutting down")

def check_for_numbers(self):

        resp = CheckNumbersResponse()
        resp.x = -1
        resp.y = -1
        resp.gotMarkers = 0

        data = rospy.wait_for_message('/camera/rgb/image_raw', Image)
        print('Grabbed a new image')

        try:

            print('converting image')
            global bridge
            cv_image = bridge.imgmsg_to_cv2(data, 'bgr8')
            print('image converted!')
        except CvBridgeError, e:
            print(e)


        corners, ids, rejected_corners = cv2.aruco.detectMarkers(cv_image,dictm,parameters=params)
            
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
                img_out = cv2.warpPerspective(cv_image, h, (img_out.shape[1],img_out.shape[0]))
                
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
                    resp.x = x
                    resp.y = y
                    resp.gotMarkers = 1
                    return resp
                else:
                    resp.gotMarkers = 1
                    print('The extracted text has is of length %d. Aborting processing' % len(text))
                    return resp
                
            else:
                print('The number of markers is not ok:',len(ids))

        else:
            print('No markers found')

        return resp

if __name__ == "__main__":
    main()
