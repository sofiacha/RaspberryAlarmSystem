#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  les5.py
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

import os
from time import sleep
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(22,GPIO.OUT)

loop_count = 0

# define a function called morsecode
def morsecode ():
    #Dot Dot Dot
    GPIO.output(22,GPIO.HIGH)
    sleep(.1)
    GPIO.output(22,GPIO.LOW)
    sleep(.1)
    GPIO.output(22,GPIO.HIGH)
    sleep(.1)
    GPIO.output(22,GPIO.LOW)
    sleep(.1)
    GPIO.output(22,GPIO.HIGH)
    sleep(.1)

    #Dash Dash Dash
    GPIO.output(22,GPIO.LOW)
    sleep(.2)
    GPIO.output(22,GPIO.HIGH)
    sleep(.2)
    GPIO.output(22,GPIO.LOW)
    sleep(.2)
    GPIO.output(22,GPIO.HIGH)
    sleep(.2)
    GPIO.output(22,GPIO.LOW)
    sleep(.2)
    GPIO.output(22,GPIO.HIGH)
    sleep(.2)
    GPIO.output(22,GPIO.LOW)
    sleep(.2)

    #Dot Dot Dot
    GPIO.output(22,GPIO.HIGH)
    sleep(.1)
    GPIO.output(22,GPIO.LOW)
    sleep(.1)
    GPIO.output(22,GPIO.HIGH)
    sleep(.1)
    GPIO.output(22,GPIO.LOW)
    sleep(.1)
    GPIO.output(22,GPIO.HIGH)
    sleep(.1)
    GPIO.output(22,GPIO.LOW)
    sleep(.7)

os.system('clear')
print "Morse Code"

loop_count = input("How many times would you like SOS to loop?: ")

while loop_count > 0:
    loop_count = loop_count - 1
    morsecode ()

