from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker
import requests
import json
import unicodedata



DATABASE_CONFIG = 'sqlite:///DB.db'
SC_CLIENT_ID = "02gUJC0hH2ct1EGOcYXQIzRFU91c72Ea"
SC_URL = "http://api.soundcloud.com/users/"

engine = create_engine(DATABASE_CONFIG, echo=True,  encoding='utf8')
engine.raw_connection().connection.text_factory = unicode
Base = declarative_base()
Session = sessionmaker()
Session.configure(bind=engine)
session = Session()

def create_user_object_command(json_object):
	command = "User( "
	for key in json_object.keys():
		val = json_object[key]
		if  val is None:
			val = "None"
		if type(val) == unicode:
			val = str(repr(''.join([i if ord(i) < 128 else ' ' for i in val]))).replace("\"","")

		
		command += "%s = \"%s\", " % (key, val)
	command = command[:-2] + ")"
	return command
	

class User(Base):
	__tablename__ = 'users' 
    
	user_id = Column(Integer, primary_key=True, autoincrement=True)
	id = Column(String)
	website  = Column(String)
	myspace_name  = Column(String)
	last_name  = Column(String)
	reposts_count  = Column(String)
	public_favorites_count  = Column(String)
	followings_count  = Column(String)
	full_name  = Column(String)
	city  = Column(String)
	first_name  = Column(String)
	track_count  = Column(String)
	playlist_count  = Column(String)
	discogs_name  = Column(String)
	followers_count  = Column(String)
	online  = Column(String)
	username  = Column(String)
	description  = Column(String)
	subscriptions  = Column(String)
	kind  = Column(String)
	last_modified  = Column(String)
	website_title  = Column(String)
	permalink_url  = Column(String)
	likes_count  = Column(String)
	permalink  = Column(String)
	country  = Column(String)
	uri  = Column(String)
	avatar_url  = Column(String)
	comments_count  = Column(String)
	plan  = Column(String)

Base.metadata.create_all(engine)


for x in range(2, 1000):
    response = requests.get(SC_URL + str(x), params ={'client_id': SC_CLIENT_ID} )
    if response.status_code != 200:
    	continue
    command = create_user_object_command(response.json())
    u = eval(command)
    session.add(u)
    
    #how many to store in the memory before commit!
    session.commit()




