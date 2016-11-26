################
## WEB KAMALA ##
##            ##
################

from IPython import embed
import csv
import requests
from collections import Counter
import pickle
import random
import string

import numpy
from keras.datasets import imdb
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Flatten
from keras.layers.embeddings import Embedding
from keras.preprocessing import sequence
from keras.models import model_from_json




kamala        = 0 # Kamala is our NN
desc_dict     = 0 # Duplicate Description Counter
web_dict      = 0 # Duplicate Website Name Counter
sketchy_terms = 0 # List of Sketchy Terms


#Load the NN and the Dictionaries
def load_everything():
    print("Loading Kamala...")
    json_file = open('kamala.json', 'r')
    loaded_model_json = json_file.read()
    json_file.close()
    loaded_model = model_from_json(loaded_model_json)
    # load weights into new model
    loaded_model.load_weights("kamala.h5")
    loaded_model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
    

    print "Loading Dictionaries..."
    f = open('desc_dict.ser','r')
    desc_dict = pickle.load(f)
    f.close()
    f = open('web_dict.ser','r')
    web_dict = pickle.load(f)
    f.close()


    print "Loading Sketchy Terms"
    sketchy_terms = [ "goo.gl" , "laid tonight", "bit.ly", " bitly ", " adfly ", "adf.ly", " porn ", " boobs ", " pornstar ", " anal ", " tits ", " nipples ", " vagina ", " penis "," viagra "," cialsis "]


    return (loaded_model,desc_dict,web_dict,sketchy_terms)

#Query the User from Soundcloud and turn it into a Feature Vector to feed into the NN
def get_user(id):

    r = requests.get("http://api.soundcloud.com/users/"+str(id)+"?client_id=02gUJC0hH2ct1EGOcYXQIzRFU91c72Ea")

    if int(r.status_code) != 200:
        print r.status_code,"Error!"
        return -1

    r = r.json()

    header =[
        "Followers",           \
        "Following",           \
        "Published",           \
        "URL",                 \
        "ProfaneDescription",  \
        "ProfaneTitle",        \
        "Action",              \
        "Pays",                \
        "DuplicateDescription",\
        "DuplicateWebsite",    \
        "website_aggregate"]

    user = [0] *  len(header)

    ##### FEATURE EXTRACTION BEGINS

    #Follower
    user[0] = int(r["followers_count"])

    #Following
    user[1] = int(r["followings_count"])

    #Has Tracks
    user[2] = int(r["track_count"])

    #Has URL
    if r["website"] != None:
        user[3] = 1


    #Has profane Language in Description and website title
    
    if (r["description"] != None): 
        desc = r["description"][2:][:-1]
    else:
        desc = "none"
    if (r["website_title"] != None):
        webt = r["website_title"][2:][:-1]
    else:
        webt = "none"

    for term in sketchy_terms:
        if term.lower() in desc.lower():
            user[4] = 1
        if term.lower() in webt.lower():
            user[5] = 1 
    #Action
    user[6] = int(r["playlist_count"]) + int(r["public_favorites_count"]) + int(r["comments_count"]) + int(r["likes_count"]) + int(r["reposts_count"]) 

    #Pays
    if (r["subscriptions"] != [] or r["plan"][:2][:-1] != "Free"):
        user[7] = 1

    #Duplicate Description
    if r["description"] != None and  r["description"] !="''":
        if desc_dict["u'"+r["description"]+"'"] > 1:
            user[8] =  desc_dict["u'"+r["description"]+"'"];

    #Duplicate Website
    if r["website"] != None and  r["website"] !="''":
        if desc_dict["u'"+r["website"]+"'"] > 1:
            user[9] = desc_dict["u'"+r["website"]+"'"];

    #Is URL aggregate site
    if r["website"] != None:
        aggregate_sites = ["goo.gl","bit.ly","ad.fly","tinyurl"]
        for term in aggregate_sites:
            if term in r["website"]:
                user[10] = 1
                #print term


    return user

#Given a user id, get it from soundcloud, and feed it into the NN to classify.
def classify_user(id):
    user = get_user(id)
    #print user
    if (user == -1):
        return -1;

    proba = kamala.predict_proba(numpy.asarray([user]),verbose=0)[0][0]
    
    return proba

#In case we wrongly labeled a user as spam/legit, you can send a fix and retrain network
def fix_user(id,label):
    if label != 0 and label != 1:
        return -1
    user = get_user(id)
    kamala.train_on_batch(numpy.asarray([user]),numpy.asarray([label]))
    print "Trained"
    return 0

#In case we want to save our modified Neural Network
def save_kamala(kamala):
    model_json = kamala.to_json()
    with open("kamala_mod.json", "w") as json_file:
        json_file.write(model_json)
    # serialize weights to HDF5
    kamala.save_weights("kamala_mod.h5")
    print("Saved kamala to disk")

#EXAMPLE USAGE
if __name__ == "__main__":
    #Load Everything
    (kamala,desc_dict,web_dict,sketchy_terms) = load_everything()

    #Check Users
    print "TESTS :-------------------------------"
    print "REAL:",100*classify_user(246928450),"%"  #Not Spam (Random Zombie User)
    print "REAL:",100*classify_user(4192879),"%"    #Not Spam (Konukoii)
    print "REAL:",100*classify_user(41922879),"%"   #Not Spam (Random Zombie User)

    print "STAR:",100*classify_user(4360546),"%"    #Not Spam (Kygo)
    print "STAR:",100*classify_user(30049192),"%"   #Not Spam (Matoma)

    print "SPAM:",100*classify_user(246928489),"%"  #Spam (Pr0n)
    print "SPAM:",100*classify_user(109687919),"%"  #Spam (Quiet)

    #fix_user(246928450,1)
    embed()

