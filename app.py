from model import *
from flask import Flask, render_template, url_for, redirect, request
app = Flask(__name__)
from database import query_user_by_email, create_user


@app.route('/', methods=['GET', 'POST'])
def signIn():
	if request.method == 'GET':
		return render_template('signIn.html')
	else:
		email = request.form['email']
		password = request.form['password']

		user = query_user_by_email(email)
		if user.password == password:
			return render_template('home.html')


@app.route('/signUp', methods=['GET', 'POST'])
def signUp():
	return render_template("signIn.html")

@app.route('/home')
def home():
	return render_template("home.html")


@app.route('/settings')
def settings():
	return render_template("settings.html")

@app.route('/reminders')
def reminders():
	return render_template("reminders.html")



if __name__ == '__main__':
	app.run(debug=True)

