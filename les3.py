#!/usr/bin/env python
# -*- coding: utf-8 -*-

from time import sleep
import os
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
#GPIO.cleanup()
GPIO.setwarnings(False)
#red led	
GPIO.setup(17,GPIO.OUT)
#blue led
GPIO.setup(27,GPIO.OUT)
#button
GPIO.setup(10,GPIO.IN, pull_up_down=GPIO.PUD_UP)
#when you press the button the leds will be turn on for five seconds
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
