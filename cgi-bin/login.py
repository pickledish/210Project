#!/usr/bin/python
##!C:/python27/python.exe
import datetime
import Cookie
import os
import cgitb
import cgi
import sqlite3

cgitb.enable()

conn = sqlite3.connect('Users.db')
c = conn.cursor()

loginForm = cgi.FieldStorage()

if('username' in loginForm and 'password' in loginForm):
	user = loginForm['username'].value
	pword = loginForm['password'].value
	c.execute("SELECT * FROM Users WHERE username=?",[user])
	all_rows = c.fetchall()
	if(len(all_rows)!=0):
		if(all_rows[0][1]==pword):
			 conn.commit()
			 conn.close()
			 stored_cookie_string = os.environ.get('HTTP_COOKIE')

			 if not stored_cookie_string:
				 cookie = Cookie.SimpleCookie()
				 cookie['session'] = str(uuid.uuid4())
				 cookie['session']['path'] = '/'
				 cookie['session']['expires'] = expires.strftime()
				 expires = datetime.datetime.utcnow() + datetime.timedelta(days=60)
			 else:
				 cookie = Cookie.SimpleCookie(stored_cookie_string)

			 print "Status: 303 See Other"
			 print "Location: http:../thanks.html"
			 print cookie
			 print
		else:
			conn.commit()
			conn.close()
			print 'Content-Type: text/html'
			print
			print '''<html>
					<head>
					<meta charset="utf-8">
					<title> ToneTone - Error </title>
					</head>
					<body>
			<p> Your username does not exist </p>
			<a href="../login.html"> Back to the form</a>
			</body>
			</html>
			'''
	else:
		conn.commit()
		conn.close()
		print 'Content-Type: text/html'
		print
		print '''<html>
				<head>
				<meta charset="utf-8">
				<title> ToneTone - Error </title>
				</head>
				<body>
		<p> Your username and password match does not exist </p>
		<a href="../login.html"> Back to the form</a>
		</body>
		</html>
		'''
else:
	conn.commit()
	conn.close()
	print 'Content-Type: text/html'
	print
	print '''<html>
			<head>
			<meta charset="utf-8">
			<title> ToneTone - Error </title>
			</head>
			<body>
			   <p> input id and password </p>
				  <a href="../login.html"> Back to the form</a>
			</body>
	</html>

	'''
