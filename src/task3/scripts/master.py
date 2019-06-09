#!/usr/bin/python
# -*- coding: utf-8 -*-

import rospy
from task3.msg import *
from task3.srv import *
#from __future__ import print_function

def finished_scouting():
	# get cylinder positions
	# get ring positions
	rospy.wait_for_service('return_positions')
	return_positions = rospy.ServiceProxy('return_positions', GetPositions)
	ringAndCylinderAttributes = return_positions()


	rospy.wait_for_service('check_numbers')
	check_for_numbers = rospy.ServiceProxy('check_numbers', CheckNumbers)
	rospy.wait_for_service('check_qr')
	check_for_numbers = rospy.ServiceProxy('check_qr', CheckQr)
	rospy.wait_for_service('evaluate_qr')


	print(a)

	#TODO

	# check all circles
	# remember the colors
	# check for qr and numbers, remember both
	# ko najde krog s qr kodo, zlouda podatke, jih vnese, zgradi
	# klasifikator. ce ze ma stevilke, nejde barvo cilindra, 
	# drgac pac gleda kroge dokler ne najde cifer

	#TODO

	# ko ma cifre in vse to, vemo barvo cilindra
	# gremo do cilindra s podano barvo, preberemo qr na njem

	#TODO

	# gremo do kroga, ki je take barve kokr pise na cilindru
	# slikamo mapo


def main():

	rospy.init_node("master")
	service = rospy.Service('start_master', GetLocation, finished_scouting)
	

	try:
		rospy.spin()
	except KeyboardInterrupt:
		print('Shutting down')


if __name__ == '__main__':
    main()