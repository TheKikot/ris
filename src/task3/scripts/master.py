#!/usr/bin/python
# -*- coding: utf-8 -*-

import rospy
from task3.msg import *
from task3.srv import *
import re
#from __future__ import print_function

global model
global features
global label

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

def finished_scouting():
	# get cylinder positions
	# get ring positions
	rospy.wait_for_service('return_positions')
	return_positions = rospy.ServiceProxy('return_positions', GetPositions)
	ringAndCylinderAttributes = return_positions()


	rospy.wait_for_service('check_numbers')
	check_for_numbers = rospy.ServiceProxy('check_numbers', CheckNumbers)
	rospy.wait_for_service('check_qr')
	check_for_qr = rospy.ServiceProxy('check_qr', CheckQr)


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
	
	# izracun vektorja
		vektorX = ringAndCylinderAttributes.ringsX[i] - ringAndCylinderAttributes.normalsX[i]
		vektorY = ringAndCylinderAttributes.ringsY[i] - ringAndCylinderAttributes.normalsY[i]
		print("razdalja: ", (vektorX**2 + vektorY**2))
	
		# premik do kroga
		ciljX = ringAndCylinderAttributes.ringsX[i] + vektorX
		ciljY = ringAndCylinderAttributes.ringsY[i] + vektorY
	
		rospy.wait_for_service('check_if_reachable')
		cir = rospy.ServiceProxy('check_if_reachable', GetColor)
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
			# gremo tja
			print("")
		else:
			# premaknemo cilj	
			ciljX = ringAndCylinderAttributes.ringsX[i] - vektorX
			ciljY = ringAndCylinderAttributes.ringsY[i] - vektorY
		
			rospy.wait_for_service('check_if_reachable')
			cir = rospy.ServiceProxy('check_if_reachable', GetColor)
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
				# gremo tja
				print("")
			else:
				print("noben cilj ni dosegljiv: ", ringAndCylinderAttributes.ringsX[i], ", ", ringAndCylinderAttributes.ringsY[i])
	
	
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
					print("")
				else:
					x=odg.x
					y=odg.y
					if(podatki == 1):
						color = get_prediction(x, y)
						break
					continue

		#ce se nimamo podatkov modela itd.
		if(podatki == None):
			odg = check_for_qr()

			if(odg.data == 'No QR codes found'):
				#ta krog je kompleten fail, morde bi blo treba neki nardit glede tega
				print("")
			elif(len(find_urls(odg.data)) > 0):
				#nasli smo qr, ki vsebuje spletno stran, kar bi tut mogu
				get_online_data(odg.data)
				podatki = 1
				build_classifier()
				if(x != None and y != None):
					color = get_prediction(x, y)
					break

	#KONC LOOPA

	# ko ma cifre in vse to, vemo barvo cilindra
	# gremo do cilindra s podano barvo, preberemo qr na njem

	#TODO - pejt do cilindra dane barve
	# 0 - red
	# 1 - green
	# 2 - blue
	# 3 - yellow

	#TODO - LOOP v katerem se premikamo okol cilindra, dokler ne preberemo QR kode
	odg = check_for_qr()
	if(odg.data == 'No QR codes found'):
		#TODO premakni se
		#continue
		print("")
	elif(len(find_urls(odg.data))>0):
		#nasli smo QR v enmu od krogov, ignore
		print("")
	else:
		barvaKroga = odg.data



	# gremo do kroga, ki je take barve kokr pise na cilindru
	# slikamo mapo

	#TODO


def main():

	rospy.init_node("master")
	service = rospy.Service('start_master', GetLocation, finished_scouting)
	

	try:
		rospy.spin()
	except KeyboardInterrupt:
		print('Shutting down')


if __name__ == '__main__':
    main()
