#!/usr/bin/env python
# -*- coding: utf-8 -*-


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
