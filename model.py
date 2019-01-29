from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine, DateTime

Base = declarative_base()

# Write your classes here :
class Users(Base):
	__tablename__ = 'users'
	id = Column(Integer, primary_key = True)
	email = Column(String)
	password = Column(String)
	first_name = Column(String)
	last_name = Column(String)

class Reminder(Base):
	__tablename__='home'
	id= Column(Integer, primary_key = True)
	where = Column(String)
	how = Column(DateTime)
	what = Column(String)

def __repr__(self):
	return ("email adress:{}, password:{}".format(self.email, self.password))
