from model import *

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///database.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def create_user(email, password, first_name, last_name):
	user = Users(email = email, password = password, first_name = first_name, last_name = last_name)
	session.add(user)
	session.commit()

def query_user_by_email(email):
	user = session.query(Users).filter_by(email = email).all()
	return user


