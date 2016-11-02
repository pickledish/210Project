#!C:/python27/python.exe
##!/usr/bin/python

import cgitb
import cgi
import sqlite3

cgitb.enable()

conn = sqlite3.connect('Users.db')

c = conn.cursor()

c.execute('CREATE TABLE IF NOT EXISTS Users(username varchar(100) primary key, password varchar(100))')

loginForm = cgi.FieldStorage()

print 'Content-Type: text/html'
print

print '''<html>
		<head>
		<meta charset="utf-8">
		<title> ToneTone - Account creation success </title>
		</head>
		<body>'''

if('username' in loginForm and 'password' in loginForm):
	user = loginForm['username'].value
	pword = loginForm['password'].value
	c.execute("SELECT * FROM Users WHERE username=?", [user])
	all_rows = c.fetchall()
	if(len(all_rows)==0):
		c.execute("INSERT INTO Users VALUES (?, ?)", (user, pword))
		conn.commit()
		conn.close()
		print '<p> Thank you, the form worked and you have an account!</p>'
		print 'username: ' + user + ' password: ' + pword
		print	'''
		<a href="../index.html"> Back to main</a>
		</body>
		</html>'''
	else:
		conn.commit()
		conn.close()
		print'<p> Your username is used by someone else already </p>'
		print'''
		<a href="../signup.html"> Back to the form</a>
		</body>
		</html>
		'''
else:
	conn.commit()
	conn.close()
	print'<p> input id and password </p>'
	print'''	<a href="../signup.html"> Back to the form</a>
		</body>
	</html>

	'''
