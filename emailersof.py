#!/usr/bin/env python
# -*- coding: utf-8 -*-
import smtplib 
smtpUser = 'YourMailHere@gmail.com'
smtpPass= 'YourPassword'

toAdd = "EmailToSend@gmail.com"
fromAdd = smtpUser

subject = 'Python Test'
header = 'To: ' + toAdd + '\n' + 'From: ' + fromAdd +'\n' + 'Subject: ' + subject
body = 'From a python script'

print header + '\n' + body

s=smtplib.SMTP('smtp.gmail.com',587)
s.ehlo()
s.starttls()
s.ehlo()

s.login(smtpUser,smtpPass)

s.sendmail(fromAdd, toAdd, header + '\n' + body)

s.quit
