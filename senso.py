#!/usr/bin/env python
# -*- coding: utf-8 -*-

import MySQLdb
import smtplib 
import os
import glob
import datetime
from time import sleep
import RPi.GPIO as GPIO

#function to send emails informative and SOS ones
def emailer(ldr,therm,subje,danger):
	
	smtpUser = 'YourEmail@gmail.com'
	smtpPass= 'YourPassword'

	toAdd = "receiver@gmail.com"
	fromAdd = smtpUser

	subject = subje
	header = 'To: ' + toAdd + '\n' + 'From: ' + fromAdd +'\n' + 'Subject: ' + subject
	if (danger==0):
		body = 'Current light value is %d. \n Current temperature is %d' %(ldr,therm)
	else:
		body = 'SOS, PIR got a motion. Someone is on the house!!!'

	print header + '\n' + body

	s=smtplib.SMTP('smtp.gmail.com',587)
	s.ehlo()
	s.starttls()
	s.ehlo()

	s.login(smtpUser,smtpPass)

	s.sendmail(fromAdd, toAdd, header + '\n' + body)

	s.quit


#insert to database both celsius and farheneit temperature values 
def insertherm(cals, farh):
	# Open database connection
	db = MySQLdb.connect("localhost","root","password","SensAlarm" )

	# prepare a cursor object using cursor() method
	cursor = db.cursor()

	# Prepare SQL query to INSERT a record into the database.
	sql = "INSERT INTO Thermometre(celsius,fahreneit) VALUES ('%d', '%d')"  %(cals, farh)
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
	
	GPIO.output(17,GPIO.HIGH)
	sleep(1)
	GPIO.output(17,GPIO.LOW)

#insert to database light sensor value
def insertlght(lght):
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
	GPIO.output(27,GPIO.HIGH)
	sleep(1)
	GPIO.output(27,GPIO.LOW)
#insert to database PIR value	
def insertpir(pir):
	# Open database connection
	db = MySQLdb.connect("localhost","root","10101991","SensAlarm" )

	# prepare a cursor object using cursor() method
	cursor = db.cursor()

	# Prepare SQL query to INSERT a record into the database.
	sql = "INSERT INTO PIR(metrhsh) VALUES ('%d')"  %(pir)
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

#count variable will help as instert to dabase every 10 seconds and send informative emails every hour 
count = 0
GPIO.setmode(GPIO.BCM)
#PIR in GPIO 7
GPIO_PIR = 7

GPIO.setwarnings(False)
GPIO.cleanup()

# Set pin as input
GPIO.setup(GPIO_PIR,GPIO.IN)
#red led
GPIO.setup(17,GPIO.OUT)
#blue led
GPIO.setup(27,GPIO.OUT)
#buzzer
GPIO.setup(22,GPIO.OUT)
#2nd red led
GPIO.setup(23,GPIO.OUT)
#button
GPIO.setup(10,GPIO.IN, pull_up_down=GPIO.PUD_UP)
#the two variables are used t detect movent in comparison with before
Current_State  = 0
Previous_State = 0
#function to read light value from sensor 
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

base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir + '28*')[0]
device_file = device_folder + '/w1_slave'
#function read temperature from file
def read_temp_raw():
    f = open(device_file, 'r')
    lines = f.readlines()
    f.close()
    return lines
#using function read_temp_raw we are reading temperature and insert it in database
def read_temp():
    lines = read_temp_raw()
    while lines[0].strip()[-3:] != 'YES':
        sleep(0.2)
        lines = read_temp_raw()
    equals_pos = lines[1].find('t=')
    if equals_pos != -1:
        temp_string = lines[1][equals_pos+2:]
        temp_c = float(temp_string) / 1000.0
        temp_f = temp_c * 9.0 / 5.0 + 32.0
        insertherm(temp_c, temp_f)
        return temp_c

"""
try:
    print "Waiting for PIR to settle ..."
    # Loop until PIR output is 0
    while GPIO.input(GPIO_PIR)==1:
        Current_State  = 0 
    print "  Ready" 
    # Loop until users quits with CTRL-C
    

# clean up gpio pins when we exit the script
except KeyboardInterrupt:
    print "  Quit" 
    # Reset GPIO settings
    GPIO.cleanup()"""




while True: 
	#reads from GPIO 
	Current_State = GPIO.input(GPIO_PIR)
	#every ten seconds reads and insert to dabase LDR, PIR and temperature values
	if count%10 ==0:
		TermReading = read_temp()
		print TermReading
		#for every reading a different led blinks
		GPIO.output(17,GPIO.HIGH)
		LDRReading = RCtime(3)
		print LDRReading
		GPIO.output(27,GPIO.HIGH)
		insertlght(LDRReading)
		print Current_State
		GPIO.output(23,GPIO.HIGH)
		insertpir(Current_State)
		sleep(1)
		GPIO.output(17,GPIO.LOW)
		GPIO.output(27,GPIO.LOW)
		GPIO.output(23,GPIO.LOW)
		GPIO.output(22,GPIO.LOW)
    	#detects if an intruder is in the house and turns on all the leds and the buzzer and sends a SOS email
	if Current_State==1 and Previous_State==0:
		# PIR is triggered
		print "  Motion detected!"
		emailer(LDRReading,TermReading,"SOS DANGER",1)
     		# Record previous state
		GPIO.output(22,GPIO.HIGH)
		GPIO.output(23,GPIO.HIGH)
		GPIO.output(27,GPIO.HIGH)
		GPIO.output(17,GPIO.HIGH)
		sleep(10)
		GPIO.output(22,GPIO.LOW)
		Previous_State=1
	elif Current_State==0 and Previous_State==1:
        # PIR has returned to ready state
		print "  Ready"
		Previous_State=0
    	# Record previous state  
	sleep(1)
	count = count + 1
	subj = "Information mail"
	#every one hour an informative mail is sent to user
	if count%360 ==0:
		d=0
		emailer(LDRReading,TermReading,subj,d)
