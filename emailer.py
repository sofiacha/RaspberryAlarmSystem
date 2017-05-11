import MySQLdb
import smtplib 
import os
import glob
import datetime
from time import sleep
import RPi.GPIO as GPIO

def emailer(ldr,therm):
	
	smtpUser = 'YourMail@gmail.com'
	smtpPass= 'YourPassword'

	toAdd = "Receiver@gmail.com"
	fromAdd = smtpUser
	#sending mail with the light sensor value and the thermometer sensor value
	subject = 'Information mail'
	header = 'To: ' + toAdd + '\n' + 'From: ' + fromAdd +'\n' + 'Subject: ' + subject
	body = 'Current light value is %d. \n Current temperature is %d' %(ldr,therm)

	print header + '\n' + body

	s=smtplib.SMTP('smtp.gmail.com',587)
	s.ehlo()
	s.starttls()
	s.ehlo()

	s.login(smtpUser,smtpPass)

	s.sendmail(fromAdd, toAdd, header + '\n' + body)

	s.quit
	
	
emailer(44,22)
emailer(66,12)
