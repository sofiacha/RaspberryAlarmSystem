#!/usr/bin/python



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
