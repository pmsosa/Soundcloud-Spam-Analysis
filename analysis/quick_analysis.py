import csv


user_id                 = 0
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

'''
~578,710

['5453', '259157843', 'None', 'None', "u'Fernandes'", '0', '0', '5', "u'Daniella Fernandes'", 'None', "u'Daniella'", '13', '1', 'None', '5', 'False', "u'Daniella Fernandes'", '"u\'Estudante de Publicidade e Propaganda da PUCRS. ']


eg.
5335,261152776,None,None,None,0,0,0,'',None,None,0,0,None,0,False,u'User 789392270',None,[],u'user',u'2016/10/13 01:02:34 +0000',None,u'http://soundcloud.com/user-789392270',0,u'user-789392270',None,u'https://api.soundcloud.com/users/261152776',u'https://a1.sndcdn.com/images/default_avatar_large.png',0,u'Free'


Things that would be interesting to find out:

=> Id: Followers/Following in Groups of 10 [0,200]
   -> For People who have beyond a certain range save them in a file as possible spam
=> File with list of websites
=> Amount of people who have websites with keywords:{ goo.gl , bit.ly, bitly, ad, adf.ly adfly, google, porn, boobs, sex, anal, tits, nipples, vagina }
=> Amount of people who have descriptions and websites with above keywords
=> # of users that still have "user-XXXXX" as their name
=> 


{"id":246928489,"kind":"user","permalink":"carolynsd-erhill","username":"Caitlin Reed","last_modified":"2016/08/12 19:04:18 +0000","uri":"https://api.soundcloud.com/users/246928489","permalink_url":"http://soundcloud.com/carolynsd-erhill","avatar_url":"https://i1.sndcdn.com/avatars-000245584247-j671gs-large.jpg","country":"Monaco","first_name":"Fiona","last_name":"Grant","full_name":"Fiona Grant","description":"Good girls do bad things sometimes! bit.ly/2aGe8ZY","city":null,"discogs_name":null,"myspace_name":null,"website":"http://goo.gl/kheXJr","website_title":"Hi! Delightful, do you want to see me naked boobs?  inPress","track_count":0,"playlist_count":0,"online":false,"plan":"Free","public_favorites_count":0,"subscriptions":[],"likes_count":0,"reposts_count":0,"comments_count":0,"followers_count":7,"followings_count":278}



'''
limit = 578710
i = 0


#1. Sketchy Followers/Following Ratio
ffclusters = [0] * 100
sketchy_clusters = 150
sketchy_ff_cluster = open("sketchy_ff_cluster.csv","w+")
#2. Sketchy Website List
sketchy_terms = [ "goo.gl" , "bit.ly", "bitly", "adfly", "adf.ly", "porn", "boobs", "sex", "anal", "tits", "nipples", "vagina", "penis"]
sketchy_website_cluster = open("sketchy_website_cluster.csv","w+")
sketchy_sites = open("sketchy_sites.csv","w+")
site_counter = 0
#3. Sketchy Description List
sketchy_description_cluster = open("sketchy_description_cluster.csv","w+")
sketchy_description = open("sketchy_description.csv","w+")
desc_counter = 0
#5. Newbie Users
newbies = 0



with open("users.csv", 'r') as f:
    reader = csv.reader(f)
    for rinput in reader:
        if (i == 0):
            i+=1;
            continue;
        i += 1;

        r = rinput
        if (len(r) != 30):
            print len(r)
            if (len(r)==1):
                print rinput;
                break;
            continue;
        
        #1. Id Followers/Following
        ffratio = 0
        if (int(r[followers_count]) == 0):
            ffratio = float(r[followings_count])
        else:
            ffratio = float(r[followings_count])/float(r[followers_count])
            
        if (int(ffratio/10) >= len(ffclusters)):
            ffclusters[len(ffclusters)-1] += 1;
        else:
            ffclusters[int(ffratio/10)] += 1;
            
        if (ffratio/10 > 150):
            sketchy_ff_cluster.write(str(rinput)+"\n");
            
        #2. Users with sketchy websites
        if (r[website] != "None"):
            for term in sketchy_terms:
                if (term in r[website] or term in r[website_title]):
                    sketchy_website_cluster.write(str(rinput)+"\n")
                    sketchy_sites.write(r[website]+" "+r[website_title]+"\n")
                    site_counter += 1
        #3. Users with sketchy description
        if (r[description] != "None"):
            for term in sketchy_terms:
                if (term in r[description]):
                    sketchy_description_cluster.write(str(rinput)+"\n")
                    sketchy_description.write(r[description]+"\n")
                    desc_counter += 1
        
        #5. Users that Still have User-XXXXX as their name

        if (("user-" in r[permalink]) and ("User " in r[username])):
            newbies += 1;
        
         
        #6. Savepoint
        if (i % 1000 == 0):
            savepoint = open("savepoint.txt","w+")
            savepoint.write("i: "+str(i)+"\n")
            savepoint.write("ffclusters: "+str(ffclusters)+"\n")
            savepoint.write("site_counter: "+str(site_counter)+"\n")
            savepoint.write("desc_counter: "+str(desc_counter)+"\n")
            
            #close all files
            sketchy_ff_cluster.close()
            sketchy_website_cluster.close()
            sketchy_sites.close()
            sketchy_description_cluster.close()
            sketchy_description.close()
            #reopen all files
            sketchy_ff_cluster = open("sketchy_ff_cluster.csv","a+")
            sketchy_website_cluster = open("sketchy_website_cluster.csv","a+")
            sketchy_sites = open("sketchy_sites.csv","a+")
            sketchy_description_cluster = open("sketchy_description_cluster.csv","a+")
            sketchy_description = open("sketchy_description.csv","a+")
            
            print "Saved at i: ",i














