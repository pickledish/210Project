# Simple database plugin for Python
from peewee import *

# Even simpler web framework for Python. @app.route() commands route URLs to functions
from flask import Flask
from flask import render_template, request, make_response

import datetime

app = Flask(__name__)
db = SqliteDatabase("UserTable.db")

# Our "User" table, it has character fields for username and password, and a date field
class User(Model):
	username = CharField()
	hashed_password = CharField()
	time_created = DateTimeField()

	class Meta:
		database = db # This model uses the "UserTable.db" database. Don't worry about this

# Function to create the tables for the first time. This is only run once, from the python3 interpreter directly
def create_tables():
    db.connect()
    db.create_tables([User])

@app.route('/', methods=['POST', 'GET'])
def index():

	# This means someone tried to log in, so we need to process it
	if (request.method == 'POST'):

		usern = request.form["username"]
		passw = request.form["password"]
		
		# See if the person exists in the database. If not, the whole thing fails cause they have no account
		try:
			this_person = User.get(User.username == usern)
		except DoesNotExist:
			return render_template("index.html", status = "failure")

		old_time = this_person.time_created
		attempted_hashed_pw = passw # TODO: No but like actually hash it

		# This will fail if their password was wrong, so we once again return with a failed state
		if (attempted_hashed_pw != this_person.hashed_password):
			return render_template("index.html", status = "failure")

		# If we made it this far, that means they exist and typed the password right, so log them in
		# We're using make_response() because apparently you can only set cookies after the template has been rendered
		rsp = make_response(render_template("index.html", loggedin = True, user = usern))

		# Here, we set up the expiration date for the cookie
		expire_date = datetime.datetime.now()
		expire_date = expire_date + datetime.timedelta(days=30)
		rsp.set_cookie('logged_in_user', usern, expires=expire_date)

		return rsp

	if ('logged_in_user' in request.cookies):
		return render_template("index.html", loggedin = True, user = request.cookies['logged_in_user'])

	else:
		return render_template("index.html", loggedin = False)

@app.route('/newAccount/', methods=['POST', 'GET'])
def makeAccount():

	# This means that someone tried to make an account, so we gotta deal with it
	if (request.method == 'POST'):

		usern = request.form["username"]
		passw = request.form["password"]
		
		# If the "get" function errors out with a DoesNotExist, that's good! So we insert a new user into it
		try:
			this_person = User.get(User.username == usern)
		except DoesNotExist:
			
			now = datetime.datetime.now()
			hashedpw = passw # TODO: No but like actually hash it please
			newUser = User(username = usern, hashed_password = hashedpw, time_created = now)
			newUser.save()

			# This is what we wanted, so we return success
			return render_template("newUser.html", status = "success")

		# The "get" function returned a user! That means there's someone in the table with this name already
		return render_template("newUser.html", status = "failure")

	return render_template("newUser.html", status = "")

@app.route('/logout/')
def logout():

	# To log a user out, we just delete their session cookie and return them to the not-logged-in index page
	rsp = make_response(render_template("logout.html"))
	rsp.set_cookie('logged_in_user', "This expires immediately", expires=0)

	return rsp

@app.route('/CEG/')
def CEGPage():

	# To log a user out, we just delete their session cookie and return them to the not-logged-in index page
	rsp = make_response(render_template("ceg.html"))

	return rsp








