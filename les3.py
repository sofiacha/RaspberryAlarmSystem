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

from time import sleep
import os
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
#GPIO.cleanup()
GPIO.setwarnings(False)
	
GPIO.setup(17,GPIO.OUT)
GPIO.setup(27,GPIO.OUT)

GPIO.setup(10,GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:	
	if (GPIO.input(10) == False):
		print "Button pressed" 
		os.system('date')
		#print GPIO.input(10)
		GPIO.output(17,GPIO.HIGH)
		GPIO.output(27,GPIO.HIGH)
		sleep(5)
	else:
		print "Wait for you to press the button!"
		os.system('clear')
		GPIO.output(17,GPIO.LOW)
		GPIO.output(27,GPIO.LOW)
		#sleep(2)

