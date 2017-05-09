#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  les2.py
#  
#  Copyright 2017  <pi@raspberrypi>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  

import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
#GPIO.cleanup()
GPIO.setwarnings(False)	
GPIO.setup(17,GPIO.OUT)
GPIO.setup(27,GPIO.OUT)
GPIO.setup(10,GPIO.IN)
time.sleep(2)
if ~(GPIO.input(10)):
	print "Lights on"
	GPIO.output(17,GPIO.HIGH)
	GPIO.output(27,GPIO.HIGH)
else:
	print "Lights off"
	GPIO.output(17,GPIO.LOW)
	GPIO.output(27,GPIO.LOW)

"""for i in range(1,11):
	print "Lights on"
	GPIO.output(17,GPIO.HIGH)
	GPIO.output(27,GPIO.HIGH)
	time.sleep(1)
	print "Lights off"
	GPIO.output(17,GPIO.LOW)
	GPIO.output(27,GPIO.LOW)
	time.sleep(1)
"""
