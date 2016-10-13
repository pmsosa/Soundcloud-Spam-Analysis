#Soundcloud User Scraper - Konuko II 
import MySQLdb,json,requests,time
import os

#Constants
SC_API = "02gUJC0hH2ct1EGOcYXQIzRFU91c72Ea"
SC_URL = "http://api.soundcloud.com/users/"


DB_USER = "CS276"
DB_NAME = "scusers"
DB_HOST = "localhost"

db = MySQLdb.connect(host=DB_HOST,user=DB_USER,db=DB_NAME)
cursor = db.cursor()

idnum = 261158010 #Starting point
counting = True

while (counting):
    #Query Soundcloud


    #eg call: http://api.soundcloud.com/users/261158010?client_id=02gUJC0hH2ct1EGOcYXQIzRFU91c72Ea
    url = SC_URL + str(idnum) + "?client_id="+ SC_API;
    print url;

    # try:
    #Make URL CALL
    resp = requests.get(url=url);
    
    #SUCCESSFUL RESPONSE
    if (resp.status_code == 200):

        data = json.loads(resp.text)


        __id = data["id"] ; 
        __permalink = data["permalink"]        
        __username = data["username"];
        __uri = data["uri"];
        __avatar_url = data["avatar_url"];         
        __country = data["country"];        
        __full_name = data["full_name"];
        __city = data["city"];
        __description = data["description"];
        __discogs_name = data["discogs_name"];         
        __myspace_name = data["myspace_name"];        
        __website = data["website"];        
        __website_title = data["website_title"];        
        __online = data["online"];        
        __track_count = data["track_count"];         
        __playlist_count = data["playlist_count"];        
        __followers_count = data["followers_count"];        
        __followings_count = data["followings_count"];        
        __public_favorites_count = data["public_favorites_count"];        
        __permalink_url = data["permalink_url"];


        # SQLquery = "INSERT INTO users (id, permalink, username, uri, avatar_url, country, full_name, city, description, discogs-name, myspace-name, website,"
        # SQLquery+="website-title, online, track_count, playlist_count, followers_count, followings_count, public_favorites_count, permalink_url)"
        # SQLquery+="VALUES ("+str(__id)+",\""+str(__permalink)+"\",\""+str(__username)+"\",\""+str(__uri)+"\",\""+str(__avatar_url)+"\",\""+str(__country)+"\",\""+str(__full_name)+"\",\""+str(__city)+"\","
        # SQLquery+="\""+str(__description)+"\",\""+str(__discogs_name)+"\",\""+str(__myspace_name)+"\",\""+str(__website)+"\",\""+str(__website_title)+"\",\""+str(__online)+"\","
        # SQLquery+="\""+str(__track_count)+"\",\""+str(__playlist_count)+"\",\""+str(__followers_count)+"\",\""+str(__followings_count)+"\",\""+str(__public_favorites_count)+"\",\""+str(__permalink_url)+"\")"

        try:
            cursor.execute("INSERT INTO users(id, permalink, username, uri, avatar_url, country, full_name, city, description, discogs_name, myspace_name, website, website_title, online, track_count, playlist_count, followers_count, followings_count, public_favorites_count, permalink_url) \
                VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (int(__id), __permalink, __username, __uri, __avatar_url, __country, __full_name, __city, __description, __discogs_name, __myspace_name, __website,__website_title, bool(__online), int(__track_count), int(__playlist_count), int(__followers_count), int(__followings_count), int(__public_favorites_count), __permalink_url))
            db.commit()
        except:
            print "I caught a duplicate error!"
             
        #cursor.execute()

    #ERROR RESPONSE
    elif (resp.status_code == 404):
        print "not found",idnum

    #THROTTLE RESPONSE
    elif (resp.status_code == 429):
        print "We Are Being Throttled! Stopped at",idnum,time.ctime()
        time.sleep(3,600) #Wait for 1h before continuing
        continue;

    #DUNNO WHAT THIS RESPONSE IS
    else:
        print resp.status_code, idnum, time.ctime()
        a = raw_input("Continue?")

    idnum = idnum - 1

    # except:
    #     print e
    #     print "Some Error! = ", idnum
    #     a = raw_input("continue?")



