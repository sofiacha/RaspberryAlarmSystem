#!/usr/bin/env python
# -*- coding: utf-8 -*-

import MySQLdb

def insert(lght):
	# Open database connection
	db = MySQLdb.connect("localhost","root","10101991","SensAlarm" )

	# prepare a cursor object using cursor() method
	cursor = db.cursor()

	# Prepare SQL query to INSERT a record into the database.
	sql = "INSERT INTO LDR(light) VALUES ('%d')"  %(lght)
	try:
	   # Execute the SQL command
	   cursor.execute(sql)
	   # Commit your changes in the database
	   db.commit()
	except:
	   # Rollback in case there is any error
	   db.rollback()

	# disconnect from server
	db.close()

import os
import datetime
from time import sleep
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

def RCtime (RCpin):
    reading = 0
    GPIO.setup(RCpin, GPIO.OUT)
    GPIO.output(RCpin, GPIO.LOW)
    sleep(.1)

    GPIO.setup(RCpin, GPIO.IN)
    # This takes about 1 millisecond per loop cycle
    while (GPIO.input(RCpin) == GPIO.LOW):
        reading += 1
    return reading

while True: 
    GetDateTime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    LDRReading = RCtime(3)
    print RCtime(3)
    insert(LDRReading)

    # Open a file
    fo = open("/home/pi/Desktop/RaspbPI/foo.txt", "wb")
    fo.write (GetDateTime)
    LDRReading = str(LDRReading)
    fo.write ("\n")
    fo.write (LDRReading)

    # Close opend file
    fo.close()
    sleep(1)
