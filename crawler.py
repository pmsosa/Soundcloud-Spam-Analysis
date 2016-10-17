from sqlalchemy.orm import sessionmaker
import requests
import json
import unicodedata
from users import User
import users



SC_CLIENT_ID = "02gUJC0hH2ct1EGOcYXQIzRFU91c72Ea"
SC_URL = "http://api.soundcloud.com/users/"
starting_user_number = 1
number_rows_to_be_committed = 10
ending_user_number = 1000000
number_of_users_to_fetch = 20


Session = sessionmaker()
Session.configure(bind=users.engine)
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
	

for x in range(starting_user_number, ending_user_number):
    response = requests.get(SC_URL + str(x), params ={'client_id': SC_CLIENT_ID} )
    if response.status_code != 200:
    	continue
    
    if number_of_users_to_fetch == 0:
    	session.commit()
    	break
    else:
    	number_of_users_to_fetch -=1

    command = create_user_object_command(response.json())
    u = eval(command)
    session.add(u)
    
    if x % number_rows_to_be_committed == 0:
    	session.commit()
