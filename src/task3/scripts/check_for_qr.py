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


global bridge 

def main():
    print("setting up node")
    rospy.init_node('check_for_qr', anonymous=False)
    global bridge
    bridge = CvBridge()

    call_srv = rospy.Service('check_qr', GetLocation, check_for_QR)

    try:
        rospy.spin()
    except KeyboardInterrupt:
        print("Shutting down")

def check_for_QR(self):
        
        for i in range(0, 5):          
            data = rospy.wait_for_message('/camera/rgb/image_raw', Image)
            print('Grabbed a new image')

            try:

                print('converting image')
                global bridge
                cv_image = bridge.imgmsg_to_cv2(data, 'bgr8')
                print('image converted!')
            except CvBridgeError, e:
                print(e)

            # 640x480

            #cv_image = cv_image[80:420, 0:640]
            cv_image_copy = cv_image.copy()

            # Set the dimensions of the image

            #self.dims = cv_image.shape

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

                    
            elif len(decodedObjects)==0:
                print("Havent found any QR codes")
                #TODO mapa
            else:
                print("Found more than 1 QR code")

        return []

if __name__ == "__main__":
    main()