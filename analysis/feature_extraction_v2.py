import csv
import requests

#Fields

id                      = 1
website                 = 2
myspace_name            = 3
last_name               = 4
reposts_count           = 5
public_favorites_count  = 6
followings_count        = 7
full_name               = 8
city                    = 9
first_name              = 10
track_count             = 11
playlist_count          = 12
discogs_name            = 13
followers_count         = 14
online                  = 15
username                = 16
description             = 17
subscriptions           = 18
kind                    = 19
last_modified           = 20
website_title           = 21
permalink_url           = 22
likes_count             = 23
permalink               = 24
country                 = 25
uri                     = 26
avatar_url              = 27
comments_count          = 28
plan                    = 29
#user_id                 = 0 #This is internal to our DB only
total_fields = 29


i = 0


music_terms = ["guitar","music","hiphop","hip-hop","techno","rock","country","pop","rap","orchestra","symphony","piano","metal","house","dubstep",  \
"jazz","reggae","musical","opera","calypso","dance","song","art","ballet","flamenco","choral","rhythm","lyric","ballad","musicians","performed","blues"]

sketchy_one_liners = ["Food evangelist"," Coffee fanatic","Wannabe analyst","Communicator","General web specialist",    \
"Alcohol scholar","Social media lover","Introvert","Total reader"," Friendly organizer","General analyst",          \
"Alcohol evangelist","Hardcore creator","Travel nerd", "Devoted entrepreneur"," Reader","Internet evangelist",      \
"General analyst","Wannabe analyst","Friendly web nerd"," Freelance social media expert","Thinker","Alcohol geek","Student","Total tv lover"]

sketchy_terms = [ "goo.gl" , "bit.ly", "bitly", "adfly", "adf.ly", "porn", "boobs", "sex", "anal", "tits", "nipples", "vagina", "penis"]

output = open("processed.csv","w+")
sketch_output = open("processed_sketch.csv","w+")

with open("cs276_NOV06-2pm.csv", 'r') as f:
    reader = csv.reader(f)
    next(reader)

    write_head = 0
    sketchnum = 0
    

    for r in reader:

        sketch = False

        user = []
        header = []

        ###Random Check!#########
        if (len(r) != 30):
            print len(r)
            if (len(r)==1):
                print rinput;
                break;
            continue;
        ##########################
       
##### FEATURE EXTRACTION BEGINS

        #ID     (Keep the User ID to be able to distinguish them)
        user += [r[id]]
        header += ["id"]

    ####### TEXT BASED FEATURES

        #Website, Myspace   (Are there sketchy terms in their websites or myspace names)
        temp = r[website] + " " + r[myspace_name] + " " + r[website_title]
        c = 0
        for term in sketchy_terms:
            if term.lower() in temp.lower():
                c = c + 1
                sketch = True
        user += [c]
        header += ["urls"]

        #Description  (Are there sketchy terms in their Description)
        temp = r[description]
        c = 0
        for term in sketchy_terms:
            if term.lower() in temp.lower():
                c = c + 1
                sketch = True
        user += [c]
        header += ["description-porn"]

        temp = r[description]
        for term in sketchy_one_liners:
            if term.lower() in temp.lower():
                c = c + 1
                sketch = True
        user += [c]
        header += ["description-sketchy"]

        #First Name
        user += [abs(hash(r[first_name]))]
        header += ["first_name"]

        #Last_Name (Hash it to find similar matches)
        user += [abs(hash(r[last_name]))]
        header += ["last_name"]
        
        #Full Name 
        user += [abs(hash(r[full_name]))]
        header += ["full_name"]

        #Username
        user += [abs(hash(r[username]))]
        header += ["username"]

        #City
        user += [abs(hash(r[city]))]
        header += ["city"]

        #Country
        user += [abs(hash(r[country]))]
        header += ["country"]

        #Avatar URL
        user += [abs(hash(r[avatar_url]))]
        header += ["avatar_url"]

    #### COUNT BASED FEATURES 

        #Repost Count
        user += [int(r[reposts_count])]
        header += ["reposts_count"]

        #Public Favs
        user += [int(r[public_favorites_count])]
        header += ["public_favorites_count"]

        #Following
        user += [int(r[followings_count])]
        header += ["followings_count"]

        #Follower Count
        user += [int(r[followers_count])]
        header += ["followers_count"]

        #Track Count
        user += [int(r[track_count])]
        header += ["track_count"]

        #Playlist Count
        user += [int(r[playlist_count])]
        header += ["playlist_count"]

        #Likes
        user += [int(r[likes_count])]
        header += ["likes_count"]     

        #Comment Count
        user += [int(r[comments_count])]
        header += ["comments_count"]      

    #### MISC FEATURES

        #Do they Pay? (subscriptions, plan)
        if (plan != "Free" and subscriptions != []):
            user += [1]
        else:
            user += [0]
        header += ["plan"]

        #Last Modified
        date = r[last_modified].split("/")
        date = date[0][2:] + date[1] + date[2][:2]

        user += [int(date)]
        header += ["date"]


        #Alive
        # try:
        #     print r[permalink_url][2:][:-1]
        #     r = requests.get(r[permalink_url][2:][:-1])
        #     user += [r.status_code]
        #     print r.status_code
        #     header += ["alive"]
        # except:
        #     raw_input("Something bad happened at user" + str(r[id]) + "--- Continue?")

        if (i % 10000 == 0): print i,sketchnum



        if write_head == 0:
            hdr = ','.join(map(str, header))
            print "HEADER: ", hdr
            output.write(hdr)
            sketch_output.write(hdr)
            write_head = 1

        user = ','.join(map(str, user))
        output.write(user)
        if sketch:  
            sketch_output.write(user)
            sketchnum += 1
        i += 1

output.close()


#Discogs + Online + Kind

'''

permalink_url           = 22
permalink               = 24

uri                     = 2


'''









