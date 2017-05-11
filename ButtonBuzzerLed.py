#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import os
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
#GPIO.cleanup()
GPIO.setwarnings(False)
#red led	
GPIO.setup(17,GPIO.OUT)
#blue led
GPIO.setup(27,GPIO.OUT)
#buzzer
GPIO.setup(22,GPIO.OUT)
#button
GPIO.setup(10,GPIO.IN, pull_up_down=GPIO.PUD_UP)
#asks for a choice between red and blue led
led = raw_input("Which led? \n 1) Red \n 2) Blue \n")

print "Push the button as many times as you wish to indicate times that a led can blink."

times = 0
start = time.time()
time.sleep(1)

print "Wait for you to press the button!"
print "You have 20 seconds"
#the led of your choise will be blinked depending on how many times you pressed the button
while True:	
	
	if (GPIO.input(10) == False):
		times = times +1
		GPIO.output(22,GPIO.HIGH)
		time.sleep(.1)
		GPIO.output(22,GPIO.LOW)
		#everytime you press the button the buzzer will inform you
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
		#red led and buzzer turn on as many times as it is indicated from the button
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
		#blue led and buzzer turn on as many times as it is indicated from the button
		GPIO.output(22,GPIO.HIGH)		
		GPIO.output(27,GPIO.HIGH)
		time.sleep(.1)
		GPIO.output(22,GPIO.LOW)
		GPIO.output(17,GPIO.LOW)
		time.sleep(1)
		GPIO.output(27,GPIO.LOW)
		time.sleep(1)
else:
	print "Something went terribly wrong!" #for incorrect input 
		





