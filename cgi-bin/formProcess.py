#!/usr/bin python

import cgitb
import cgi
import sqlite3

cgitb.enable()

conn = sqlite3.connect('Users.db')
c = conn.cursor()

loginForm = cgi.FieldStorage()

if ('username' in form and 'password' in form):
	user = form['username']
	pword = form['password']

	c.execute("SELECT FROM Users * WHERE username=?", user)
	all_rows = c.fetchall()

	if (!all_rows):
		c.execute("INSERT INTO Users VALUES (?, ?)", user, pword)
		print 'Content-Type: text/html'
		print
		print '''<html>
		    <head>
		        <title>Your account has been created!</title>
		    </head>
		    <body>
		        User 
		    </body>
		</html>'''


	else:
		print ("You already had an account dumbass")