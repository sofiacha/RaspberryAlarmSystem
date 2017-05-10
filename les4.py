#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  les4.py
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
import os
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
#GPIO.cleanup()
GPIO.setwarnings(False)
	
GPIO.setup(17,GPIO.OUT)
GPIO.setup(27,GPIO.OUT)
GPIO.setup(22,GPIO.OUT)

GPIO.setup(10,GPIO.IN, pull_up_down=GPIO.PUD_UP)

led = raw_input("Which led? \n 1) Red \n 2) Blue \n")

print "Push the button as many times as you wish to indicate times that a led can blink."

times = 0
start = time.time()
time.sleep(1)

print "Wait for you to press the button!"
print "You have 20 seconds"

while True:	
	
	if (GPIO.input(10) == False):
		times = times +1
		GPIO.output(22,GPIO.HIGH)
		time.sleep(.1)
		GPIO.output(22,GPIO.LOW)
		
		if times==1:
			print "Button pressed %s time" %(times) 
		else:
			print "Button pressed %s times" %(times) 
		time.sleep(0.5)

	if (time.time() - start > 20):
		print "Time 's up"
		break
		
	
if (led.lower() == "red") :
	print "Red started blinking"
	for i in range(1,times+1):
		GPIO.output(22,GPIO.HIGH)		
		GPIO.output(17,GPIO.HIGH)
		time.sleep(.1)
		GPIO.output(22,GPIO.LOW)
		GPIO.output(27,GPIO.LOW)
		time.sleep(1)
		GPIO.output(17,GPIO.LOW)
		time.sleep(1)
elif (led.lower() == "blue"):
	print "Blue started blinking"
	for i in range(1,times+1):
		GPIO.output(22,GPIO.HIGH)		
		GPIO.output(27,GPIO.HIGH)
		time.sleep(.1)
		GPIO.output(22,GPIO.LOW)
		GPIO.output(17,GPIO.LOW)
		time.sleep(1)
		GPIO.output(27,GPIO.LOW)
		time.sleep(1)
else:
	print "Something went terribly wrong!"
		





