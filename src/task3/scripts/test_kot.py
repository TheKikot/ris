#!/usr/bin/python
# -*- coding: utf-8 -*-

import math

def poslji_cilj2(nX, nY, kX, kY):

	dist = ((nX-kX)**2 + (nY-kY)**2)**(1.0/2.0)
	kot = math.asin( (nY-kY) /  dist)
	if(kX < nX):
		kot = math.pi - kot

	print(kot)


poslji_cilj2(0, 0, 2, 3)
poslji_cilj2(0, 0, 2, -3)
poslji_cilj2(0, 0, -2, -3)
poslji_cilj2(0, 0, -2, 3)