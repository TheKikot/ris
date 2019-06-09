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

global model
global features
global label

def get_online_data(url):
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


def build_classifier():
    global model, features, label
    model = KNeighborsClassifier(n_neighbors = 5)
    model.fit(features, label)


def get_prediction(x, y):
    global model
    return model.predict([[x,y]])

def main():
    print("setting up node")
    rospy.init_node('check_for_qr', anonymous=False)
    global bridge
    bridge = CvBridge()

    call_srv = rospy.Service('check_qr', CheckQr, check_for_QR)
    eval_srv = rospy.Service('evaluate_numbers', EvaluateQr, evaluate_numbers)

    try:
        rospy.spin()
    except KeyboardInterrupt:
        print("Shutting down")

def evaluate_numbers(d):
    print('evaluating for: ', d.x, d.y)

    res = EvaluateQrResponse()
    res.barva = -1

    if model == None:
        return res

    res.barva = get_prediction(d.x, d.y)
    return res

def check_for_QR(self):

        resp = CheckQrResponse()
        resp.data = "No QR codes found"
        
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
            #cv_image_copy = cv_image.copy()

            # Set the dimensions of the image

            #self.dims = cv_image.shape

            # Tranform image to gayscale

            #gray = cv2.cvtColor(cv_image, cv2.COLOR_BGR2GRAY)


            # Do histogram equlization

            #img = cv2.equalizeHist(gray)


            # Binarize the image
            # ret, thresh = cv2.threshold(img, 50, 255, 0)

            #thresh = cv2.adaptiveThreshold(
            #    img,
            #    255,
            #    cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
            #    cv2.THRESH_BINARY,
            #    151,
            #    2,
            #    )

            #kernel = np.ones((3, 3), np.uint8)

            #thresh = cv2.dilate(thresh, kernel, iterations = 1)
            #cv2.waitKey(0)


            
            print("Looking for QR codes")
            # Find a QR code in the image
            decodedObjects = pyzbar.decode(cv_image)
            #cv2.imwrite('cv_image_copy.png',
            #            cv_image)
            
            #print(decodedObjects)


            
            if len(decodedObjects) == 1:
                dObject = decodedObjects[0]
                print("Found 1 QR code in the image!")
                print("Data: ", dObject.data,'\n') 
                resp.data = dObject.data
                break                    
            elif len(decodedObjects)==0:
                print("Havent found any QR codes")
                #TODO mapa
            else:
                print("Found more than 1 QR code")

        return resp

if __name__ == "__main__":
    main()