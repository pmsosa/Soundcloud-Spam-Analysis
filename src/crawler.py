from sqlalchemy.orm import sessionmaker
import requests
import json
import unicodedata
from users import User
import users
import datetime
import logging
import argparse
import backoff


global SC_CLIENT_ID
global SC_URL


parser = argparse.ArgumentParser()
parser.add_argument("-b", "--begining_number", nargs='?', const=0,  help="set staring user number", type= int)
parser.add_argument("-e", "--ending_number",  nargs='?', const=0,  help="set ending user number", type= int)
parser.add_argument("-c", "--users_count",  nargs='?', const=10000000, default=10000000,    help="set the amount of users to be fetched", type= int)
args = parser.parse_args()


SC_CLIENT_ID = "02gUJC0hH2ct1EGOcYXQIzRFU91c72Ea"
SC_URL = "http://api.soundcloud.com/users/"
starting_user_number = args.begining_number #261158010
number_rows_to_be_committed = 100
ending_user_number = args.ending_number
number_of_users_to_fetch = args.users_count

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


@backoff.on_exception(backoff.expo,
                      (requests.exceptions.Timeout,
                       requests.exceptions.ConnectionError),
                      max_tries=30)
def make_request(user_id):
    return requests.get(SC_URL + str(x), params ={'client_id': SC_CLIENT_ID} )

x = starting_user_number
while (x > ending_user_number):
    print "ID:",x,
    response = make_request(x)
    print response.status_code
    #logging.debug("%s: Too many requests, id = %s" % (datetime.datetime.now(),x))
    
    if response.status_code != 200:
        if response.status_code != 429:
            x = x-1; #Keep decreasing counter
            continue
        while response.status_code == 429:
            sleep(random.randint(1,10 ))
            response = make_request(x)

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

    x = x-1; #Decrease Counter
