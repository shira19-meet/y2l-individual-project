from model import *

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///databases5.db?check_same_thread=False')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def create_user(email, password, first_name, last_name):
	user = Users(email = email, password = password, first_name = first_name, last_name = last_name)
	session.add(user)
	session.commit()

def get_all_users():
	users= session.query(User).all()
	return user

def query_user_by_email(email):
	user = session.query(Users).filter_by(email = email).all()
	return user

def query_user_by_first_name(first_name):
	user = session.query(Users).filter_by(first_name=first_name).first()
	return user

def query_user_by_last_name(last_name):
	user = session.query(Users).filter_by(last_name=last_name).first()
	return user

def query_users_by_password(password):
	users = session.query(Users).filter_by(password=password.all())
	return user


def add_reminder(where, how, what):
	reminder_object = Reminder(
		where=where,
		how=how,
		what=what)
	session.add(reminder_object)
	session.commit()

def get_reminders():
	reminders = session.query(Reminder).all()
	return reminders

p = get_reminders()
for a in p:
	print(a)
