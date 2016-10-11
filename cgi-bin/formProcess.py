#!/usr/bin/env python

import cgitb
import cgi
import sqlite3

cgitb.enable()

conn = sqlite3.connect('Users.db')
c = conn.cursor()

loginForm = cgi.FieldStorage()

if ('username' in loginForm and 'password' in loginForm):
	user = loginForm['username'].value
	pword = loginForm['password'].value
    

	c.execute("SELECT * FROM users WHERE username=?", [user])
	all_rows = c.fetchall()

	if (not all_rows):
		c.execute("INSERT INTO Users VALUES (?, ?)", (user, pword))
		conn.commit()
		conn.close()
		print ('Content-Type: text/html')
		print ()
		print ('''<html>
			<head>
			<meta charset="utf-8">
			<title> ToneTone - thanks </title>
			</head>
			<body>
			<p> Thank you, the form worked and you have an acceount!</p>
			<a href="index.html"> Back to the form</a>
			</body>
		</html>''')


	else:
		print ("You already had an account dumbass")