#!C:\Python27\python.exe -u

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
        if(all_rows[1]==pword):
		     conn.commit()
		     conn.close()
             print "Status: 303 See Other"
		     print "Location: http:../thanks.html"
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
    		<a href="../signin.html"> Back to the form</a>
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
		<a href="../signin.html"> Back to the form</a>
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
	              <a href="../signin.html"> Back to the form</a>
		    </body>
	</html>

	'''
