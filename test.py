import MySQLdb
import smtplib 
import os
import glob
import datetime
from time import sleep
import RPi.GPIO as GPIO

def emailer(ldr,therm):
	
	smtpUser = 'pi.joomla.solutions@gmail.com'
	smtpPass= '10Oct1991'

	toAdd = "pi.joomla.solutions@gmail.com"
	fromAdd = smtpUser

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
