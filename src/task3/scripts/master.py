#!/usr/bin/python
# -*- coding: utf-8 -*-

import rospy
from task3.msg import *
from task3.srv import *
import re
import actionlib
import math
import urllib2
from sklearn.neighbors import KNeighborsClassifier
from tf.transformations import quaternion_from_euler, euler_from_quaternion
from actionlib_msgs.msg import GoalStatus
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
from geometry_msgs.msg import PointStamped, Vector3, Pose, Twist, Quaternion, PoseWithCovarianceStamped
#from __future__ import print_function

global model
global features
global label
global ac


def find_urls(string): 
    # findall() has been used  
    # with valid conditions for urls in string 
    url = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\), ]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', string) 
    return url 

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
    
    
'''
def poslji_cilj(x, y, vektorX, vektorY):

	#print(x)
	#print(y)
	#print(vektorX)
	#print(vektorY)
	global ac
	goal = MoveBaseGoal()
	orientacija = Quaternion()
	orientacija = quaternion_from_euler(0.0, 0.0, math.asin( vektorY / ((vektorX**2 + vektorY**2)**(1/2)) ))
	#print(orientacija)
	
	goal.target_pose.header.frame_id = "map" 
	goal.target_pose.header.stamp = rospy.Time.now()
	goal.target_pose.pose.position.x = x
	goal.target_pose.pose.position.y = y
	goal.target_pose.pose.orientation.x = orientacija[0]
	goal.target_pose.pose.orientation.y = orientacija[1]
	goal.target_pose.pose.orientation.z = orientacija[2]
	goal.target_pose.pose.orientation.w = orientacija[3]
	print("pošiljam cilj: (", goal.target_pose.pose.position.x, ", ", goal.target_pose.pose.position.y, ")")
	ac.send_goal(goal)
	goal_state = ac.get_state()
	while (goal_state == GoalStatus.PENDING or goal_state == GoalStatus.ACTIVE):
		ac.wait_for_result(rospy.Duration(2.0))
		#print("goal_state: ", goal_state)
		goal_state = ac.get_state()
	#print("goal_state_fin: ", goal_state)
'''

def poslji_cilj2(nX, nY, kX, kY):
	global ac
	goal = MoveBaseGoal()
	orientacija = Quaternion()
	dist = ((nX-kX)**2 + (nY-kY)**2)**(1.0/2.0)
	kot = math.asin( (nY-kY) /  dist)
	if(kX < nX):
		kot = math.pi - kot
	kot = kot * (-1.0)
	#print(orientacija)

	orientacija = quaternion_from_euler(0.0, 0.0, kot)
	
	goal.target_pose.header.frame_id = "map" 
	goal.target_pose.header.stamp = rospy.Time.now()
	goal.target_pose.pose.position.x = nX
	goal.target_pose.pose.position.y = nY
	goal.target_pose.pose.orientation.x = orientacija[0]
	goal.target_pose.pose.orientation.y = orientacija[1]
	goal.target_pose.pose.orientation.z = orientacija[2]
	goal.target_pose.pose.orientation.w = orientacija[3]
	print("pošiljam cilj: (", goal.target_pose.pose.position.x, ", ", goal.target_pose.pose.position.y, ")")
	ac.send_goal(goal)
	goal_state = ac.get_state()
	while (goal_state == GoalStatus.PENDING or goal_state == GoalStatus.ACTIVE):
		ac.wait_for_result(rospy.Duration(2.0))
		#print("goal_state: ", goal_state)
		goal_state = ac.get_state()
	#print("goal_state_fin: ", goal_state)
	


def finished_scouting(dabe):

	
	# get cylinder positions
	# get ring positions
	rospy.wait_for_service('return_positions')
	return_positions = rospy.ServiceProxy('return_positions', GetPositions)
	ringAndCylinderAttributes = return_positions()


	rospy.wait_for_service('check_numbers')
	check_for_numbers = rospy.ServiceProxy('check_numbers', CheckNumbers)
	rospy.wait_for_service('check_qr')
	check_for_qr = rospy.ServiceProxy('check_qr', CheckQr)

	rospy.wait_for_service('check_if_reachable')
	cir = rospy.ServiceProxy('check_if_reachable', GetColor)


	x = None
	y = None
	color = None
	podatki = None
	barvaKroga = None

	#TODO

	# check all circles
	# remember the colors
	# check for qr and numbers, remember both
	# ko najde krog s qr kodo, zlouda podatke, jih vnese, zgradi
	# klasifikator. ce ze ma stevilke, nejde barvo cilindra, 
	# drgac pac gleda kroge dokler ne najde cifer


	#LOOP cez vse kroge
	for i in range(0, len(ringAndCylinderAttributes.ringsX)):
		#TODO-pejt do kroga, pocaki da pride do kroga
	
		# premik do kroga
		ciljX = ringAndCylinderAttributes.normalsX[i]
		ciljY = ringAndCylinderAttributes.normalsY[i]
	
		print("preverjam če je ", ciljX, ciljY, " dosegljiv.")

		message = GetColorRequest()
		message.cam_X = 0.0
		message.cam_Y = 0.0
		message.cam_Z = 0.0
		message.map_X = ciljX
		message.map_Y = ciljY
		message.map_Z = 0.0

		response = cir(message)
		res = response.color
		if(res == 1):
			print("cilj je dosegljiv")
			# gremo tja
			poslji_cilj2(ciljX, ciljY, ringAndCylinderAttributes.ringsX[i], ringAndCylinderAttributes.ringsY[i])
		else:
			print("cilj ni dosegljiv")
		
	
		#ce se nimamo stevilk
		if(x == None or y == None):
			#preglej za stevilke
			odg = check_for_numbers()
			if(odg.gotMarkers == 0):
				#ni uspel prebrat markerjev na sliki, mejbi kej nardimo glede tega
				print('Ne najdem primernega stevila markerjev. ')
				
			else:
				#prebral markerje, poskusal prebrat cifre
				if(odg.x == -1 or odg.y == -1):
					#prebral markerje, ampak ni prebral stevilk, najbrz qr krogec
					print("Nasel markerje, nisem prebral stevilk")
				else:
					x=odg.x
					y=odg.y
					print("prebral stevilke: ", x, y)
					if(podatki == 1):
						color = get_prediction(x, y)
						print("Dobil color: ", color)
						break
					continue
		
		#ce se nimamo podatkov modela itd.
		if(podatki == None):
			print("iscem qr kode")
			odg = check_for_numbers()
			if(odg.gotMarkers == 0):
				#ni uspel prebrat markerjev
				print('ne najdem markerjev (QR)')

				
			odg = check_for_qr()

			if(odg.data == 'No QR codes found'):
				#ta krog je kompleten fail, morde bi blo treba neki nardit glede tega
				print("Nisem nasel nobene QR kode")
			elif(len(find_urls(odg.data)) > 0):
				#nasli smo qr, ki vsebuje spletno stran, kar bi tut mogu
				print("nasel qr kodo za spletno stran")
				get_online_data(odg.data)
				podatki = 1
				build_classifier()
				print("zgradil classifier")
				if(x != None and y != None):
					color = int(get_prediction(x, y)[0])
					break

	#KONC LOOPA

	# ko ma cifre in vse to, vemo barvo cilindra
	# gremo do cilindra s podano barvo, preberemo qr na njem
	print("iscemo cilinder barve ", color)


	cilinderX = 10000
	cilinderY = 10000

	for i in range(0,len(ringAndCylinderAttributes.cylnsColor)):
		if(ringAndCylinderAttributes.cylnsColor[i] == color):
			print("nasli smo cilinder prave barve")
			print("cilinderX: ", ringAndCylinderAttributes.cylnsX[i])
			print("cilinderY: ", ringAndCylinderAttributes.cylnsY[i])
			cilinderX = ringAndCylinderAttributes.cylnsX[i]
			cilinderY = ringAndCylinderAttributes.cylnsY[i]
			break;
	else:
		print("nismo nasli cilindra prave barve :( ")



	oddaljenost = 0.6
	for i in range(0,12):
		cilyX = cilinderX + (math.sin((math.pi/6.0)*i) * oddaljenost)
		cilyY = cilinderY + (math.cos((math.pi/6.0)*i) * oddaljenost)

	
		print("preverjam ce je ", ciljX, ciljY, " dosegljiv. to je ", i, "ti od 12ih ciljev okoli valja")
		message = GetColorRequest()
		message.cam_X = 0.0
		message.cam_Y = 0.0
		message.cam_Z = 0.0
		message.map_X = ciljX
		message.map_Y = ciljY
		message.map_Z = 0.0

		response = cir(message)
		res = response.color
		if(res == 1):
			print("cilj je dosegljiv")
			# gremo tja
			poslji_cilj2(ciljX, ciljY, cilinderX, cilinderY)

			odg = check_for_qr()
			if(odg.data == 'No QR codes found'):
				#TODO premakni se
				#continue
				print("Ni qr kode")
			elif(len(find_urls(odg.data))>0):
				#nasli smo QR v enmu od krogov, ignore
				print("Qr koda vsebuje URL, torej je napacna")
			else:
				barvaKroga = odg.data
				print("Nasli barvo kroga: ", barvaKroga)
		else:
			print("cilj ni dosegljiv")
			continue


	# gremo do kroga, ki je take barve kokr pise na cilindru
	# slikamo mapo

	#TODO
	
	
	return []


def main():
	global ac
	rospy.init_node("master")
	service = rospy.Service('start_master', GetLocation, finished_scouting)
	ac = actionlib.SimpleActionClient("move_base", MoveBaseAction)
	while(not ac.wait_for_server(rospy.Duration.from_sec(3.0))):
		rospy.loginfo("Waiting for the move_base action server to come up")

	try:
		rospy.spin()
	except KeyboardInterrupt:
		print('Shutting down')


if __name__ == '__main__':
    main()
