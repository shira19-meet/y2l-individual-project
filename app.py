from model import *
from flask import Flask, render_template, url_for, redirect, request, session
import datetime

import database as db

app = Flask(__name__)
app.config["SECRET_KEY"] = "secret-key"

@app.route('/', methods=['GET', 'POST'])
def signIn():
	if request.method == 'GET':
		if "logged_in" in session:
			return redirect(url_for("home"))
		return render_template('signIn.html')
	else:
		email = request.form['email']
		password = request.form['password']

		user = db.query_user_by_email(email)
		if len(user) > 0 and user[0].password == password:
			session["logged_in"] = True
			return render_template('home.html')
		else: 
			return "User does not exist"


@app.route('/signUp', methods=['GET', 'POST'])
def signUp():
	if request.method == "GET":
		return render_template("signIn.html")
	else:
		firstname = request.form["firstname"]
		lastname = request.form["lastname"]
		password = request.form["password"]
		email = request.form["email"]
		db.create_user(email, password, first_name=firstname, last_name=lastname)
		return redirect(url_for("home"))


@app.route('/home')
def home():
	if "logged_in" not in session:
		return redirect(url_for("signIn"))
	return render_template("home.html")


@app.route('/settings')
def settings():
	if "logged_in" not in session:
		return redirect(url_for("signIn"))
	return render_template("settings.html")

@app.route('/reminders')
def reminders():
	if "logged_in" not in session:
		return redirect(url_for("signIn"))
	reminders = db.get_reminders()
	return render_template("reminders.html", reminders=reminders)

@app.route("/add-reminder", methods=["POST"])
def add_reminder():
	where = request.form["where"]
	what = request.form["what"]
	how = int(request.form["how"])
	current = datetime.datetime.now()
	hours = int(current.hour)+how
	#minutes = hours%60
	#seconds = minutes%60
	#minutes = seconds//60
	hours = hours%24
	#hours = minutes//60
	
	days = hours//24
	

	current.replace(hour=hours)
	#current.replace(minute = minutes)
	#current.replace(second=secondes)
	current.replace(day = current.day+days)
	db.add_reminder(where, current, what)

	return redirect(url_for("reminders"))
	


@app.route("/logout")
def logout():
	if "logged_in" in session:
		del session["logged_in"]
	return redirect(url_for("signIn"))

if __name__ == '__main__':
	app.run(debug=True)

