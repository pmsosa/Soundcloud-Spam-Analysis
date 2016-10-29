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


SC_CLIENT_ID = "02gUJC0hH2ct1EGOcYXQIzRFU91c72Ea"
SC_URL = "http://api.soundcloud.com/users/"

number_rows_to_be_committed = 50
number_of_users_to_fetch = 30

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
def make_request_sound_cloud(user_id):
    return requests.get(SC_URL + str(x), params ={'client_id': SC_CLIENT_ID} )

@backoff.on_exception(backoff.expo,
                      (requests.exceptions.Timeout,
                       requests.exceptions.ConnectionError),
                      max_tries=30)
def make_request_ticket():
    return requests.get('http://159.203.182.16:3000/ticket/fetch_ticket')


@backoff.on_exception(backoff.expo,
                      (requests.exceptions.Timeout,
                       requests.exceptions.ConnectionError),
                      max_tries=30)
def make_request_ticket_close(ticket_num):
    return requests.get('http://159.203.182.16:3000/ticket/close_ticket/%s' % ticket_num)






while True:
    data = make_request_ticket().json()
    starting_user_number = int(data['value'])
    ending_user_numbr = starting_user_number
    x = starting_user_number + 1000
    while (x > ending_user_numbr):
        print "\t\t\t\t\t\t\t\tID:",x,
        response = make_request_sound_cloud(x)
        print response.status_code
        #logging.debug("%s: Too many requests, id = %s" % (datetime.datetime.now(),x))
        
        if response.status_code != 200:
            if response.status_code != 429:
                x = x-1; #Keep decreasing counter
                continue
            while response.status_code == 429:
                sleep(random.randint(1,10 ))
                response = make_request_sound_cloud(x)

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
    make_request_ticket_close(data['id'])