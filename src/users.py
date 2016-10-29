from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy import *
import yaml

global engine

with open("config.yml", 'r') as ymlfile:
    cfg = yaml.load(ymlfile)
Base = declarative_base()

class User(Base):
	__tablename__ = 'users_dyno' 
    
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

engine = create_engine(cfg['active_database_config'], echo=False,  encoding='utf8')
Base.metadata.create_all(engine)
