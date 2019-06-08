#!/usr/bin/python
# -*- coding: utf-8 -*-

import rospy
from task3.msg import *

def finished_scouting():
	# get cylinder positions
	# get ring positions

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


	service = rospy.service('start_master', GetLocation, finished_scouting)

    try:
        rospy.spin()
    except KeyboardInterrupt:
        print('Shutting down')

    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()