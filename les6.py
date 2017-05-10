#!/usr/bin/env python
# -*- coding: utf-8 -*-
 

import os
import MySQLdb



def insert(cals, farh):
	# Open database connection
	db = MySQLdb.connect("localhost","root","10101991","SensAlarm" )

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


import glob
from time import sleep

base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir + '28*')[0]
device_file = device_folder + '/w1_slave'

def read_temp_raw():
    f = open(device_file, 'r')
    lines = f.readlines()
    f.close()
    return lines

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
        insert(temp_c, temp_f)
        return temp_c, temp_f

while True:
    print(read_temp()) 
    sleep(10)
