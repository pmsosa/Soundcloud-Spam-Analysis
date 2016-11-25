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
desc_dict = Counter()
web_dict = Counter()


sketchy_one_liners = ["Food evangelist","Unapologetic Analyst","Coffee fanatic","Wannabe analyst""General web specialist",    \
"Alcohol scholar","Social media lover","Introvert.","Total reader"," Friendly organizer","General analyst",              \
"Alcohol evangelist","Hardcore creator","Travel nerd", "Devoted entrepreneur","Internet evangelist",                    \
"General analyst","Wannabe analyst","Friendly web nerd","Freelance social media expert","Alcohol geek",                \
"Freelance student","Alcohol fanatic","Hipster-friendly twitter guru","Total tv lover","Incurable coffee maven"         \
"Internet evangelist","Twitter junkie","Evil student", "Zombie Ninja", "Friendly music aficionado"]

sketchy_terms = [ "goo.gl" , "laid tonight", "bit.ly", " bitly ", " adfly ", "adf.ly", " porn ", " boobs ", " pornstar ", " anal ", " tits ", " nipples ", " vagina ", " penis "," viagra "," cialsis "]




#Build Description Dictionary
if (False):
    print "Build Dictionary"
    with open("cs276_NOV06-2pm.csv", 'r') as f:
        reader = csv.reader(f)
        next(reader)

        for r in reader:
            desc_dict[r[description]] += 1
            web_dict[r[website]] += 1

            if (i % 10000 == 0): print str(i)
            i += 1

    f = open('desc_dict.ser','w')
    pickle.dump(desc_dict,f)
    f.close()
    f = open('web_dict.ser','w')
    pickle.dump(web_dict,f)
    f.close()
else:
    print "Loading Dicts..."
    f = open('desc_dict.ser','r')
    desc_dict = pickle.load(f)
    f.close()
    f = open('web_dict.ser','r')
    web_dict = pickle.load(f)
    f.close()



#Actual Feature Vectors
if (False):
    
    output = open("processed.csv","w+")
    output2 = open("sketch.csv","w+")
    
    print "Build Feature Vector"
    with open("cs276_NOV06-2pm.csv", 'r') as f:
        reader = csv.reader(f)
        next(reader)

        sketch_n = 0
        i=0
        header =["ID",                 \
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
                "Spam"]

        hdr = ','.join(map(str, header))
        output.write(hdr)

        for r in reader:

            sketch = False



            user = [0] *  len(header)

            ###Random Check!#########
            if (len(r) != 30):
                print len(r)
                if (len(r)==1):
                    print rinput;
                    break;
                continue;
            ##########################
           
        ##### FEATURE EXTRACTION BEGINS

            #ID
            user[0] = int(r[id])

            #Follower
            user[1] = int(r[followers_count])

            #Following
            user[2] = int(r[followings_count])

            #Has Tracks
            user[3] = int(r[track_count])

            #Has URL
            if r[website] != "None":
                user[4] = 1

            #Has profane Language in Description and website title
            desc = r[description][2:][:-1]
            webt = r[website_title][2:][:-1]

            for term in sketchy_terms:
                if term.lower() in desc.lower():
                    user[5] = 1
                if term.lower() in webt.lower():
                    user[6] = 1 
            #Action
            user[7] = int(r[playlist_count]) + int(r[public_favorites_count]) + int(r[comments_count]) + int(r[likes_count]) + int(r[reposts_count]) 

            #Pays
            if (r[subscriptions] != "[]" or r[plan][:2][:-1] != "Free"):
                user[8] = 1

            #Duplicate Description
            if r[description] != "None" and  r[description] !="''" and r[description] !="' '" and r[description] !="u'.'" and r[description] !="u':)'" and r[description] !="u'<3'" and r[description] != "u'...'" and r[description] !="u'I love music'":
                if desc_dict[r[description]] > 1:
                    user[9] =  desc_dict[r[description]];

            #Duplicate Website
            if r[website] != "None" and  r[website] !="''" and r[website] != "' '":
                if desc_dict[r[website]] > 1:
                    user[10] =  desc_dict[r[website]];


            # #Help with the manual pickin's. Mark potential spam that we have already seen in clusters.s
            reason = 0
            if user[9] >= 50 or user[10] >= 50: 
                user[11] = 1
                reason = 1

            replace_punctuation = string.maketrans(string.punctuation, ' '*len(string.punctuation))
            desc = desc.translate(replace_punctuation)

            for term in (["goo.gl","goo gl","bit.ly","bit ly","tinyurl","naked","boobs" ,"click here to see me","Hi sweety" ,"Hi sweetie"] +sketchy_one_liners):
                if term.lower() in desc.lower():
                    user[11] = 1
                    reason = "----2"+term+"------"
                if term.lower() in webt.lower():
                    user[11] = 1
                    reason = 3
                    
            # #######

            # if int(r[id]) == 260802509: 
            #     print desc
            #     print webt.lower()
            #     print "goo gl" in webt.lower()
            #     print user

            userW = ','.join(map(str, user))
            output.write(userW + "\n")

            if user[11] == 1:
                sketch_n += 1
                #print reason,r
                output2.write(userW + "\n")


            if (i % 10000 == 0): print str(i),str(sketch_n),"\t\t" , user
            i += 1



    output.close()
    output2.close()



#Get Batches
def getBatches(size_train,size_test,seed=0):

    random.seed(seed)
    X_train = []
    y_train = []
    X_test = []
    y_test = []

    good_train = size_train/2
    good_test = size_test/2
    bad_train = size_train/2
    bad_test = size_test/2

    with open("processed.csv","r") as f:
        reader = csv.reader(f)
        next(reader)

        for r in reader:

            for j in range(0,len(r)):
                r[j]=int(r[j])

            if (random.randint(0,1)):
                if (random.randint(0,1)):
                    #print good_test,bad_test,good_train,bad_train
                    if (r[11] == 0 and good_train > 0):
                        X_train += [r[1:-1]]
                        y_train += [r[len(r)-1]]
                        good_train -= 1
                else:

                    if (r[11] == 0 and good_test > 0):
                        X_test += [r[1:-1]]
                        y_test += [r[len(r)-1]]
                        good_test -= 1

            if good_test == good_train == 0: break;
            #print len(X_train),len(X_test)

    with open("sketch.csv","r") as f:
        reader = csv.reader(f)
        next(reader)

        for r in reader:

            for j in range(0,len(r)):
                r[j]=int(r[j])

                if (random.randint(0,1)):
                    #print good_test,bad_test,good_train,bad_train
                    if (r[11] == 1 and bad_train > 0):
                        X_train += [r[1:-1]]
                        y_train += [r[len(r)-1]]
                        bad_train -= 1
                else:

                    if (r[11] == 1 and bad_test > 0):
                        X_test += [r[1:-1]]
                        y_test += [r[len(r)-1]]
                        bad_test -= 1

            if bad_test == bad_train == 0: break;
    
    print "Training",len(X_train),"g:",good_train,"b:",bad_train
    print "Test",len(X_test),"g:",good_test,"b:",bad_test

    return (X_train,y_train,X_test,y_test)

#Keras NN
def keras_nn(X_train,y_train,X_test,y_test,verbose=0,batchsize=50,layersize=250,epoch=3,hidden=1):

    #print numpy.asarray(X_train)[0:5]
    # create the model
    model = Sequential()
    #print X_train
    model.add(Dense(layersize, activation='relu',input_dim=len(X_train[0])))
    for h in range(1,hidden):
        model.add(Dense(layersize, activation='relu'))
    model.add(Dense(1, activation='sigmoid'))
    model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
    if (verbose == 1):
        print(model.summary())

    #Fit
    model.fit(X_train, y_train, validation_data=(X_test, y_test), nb_epoch=epoch, batch_size=batchsize, verbose=verbose)
    # Final evaluation of the model
    score_test = model.evaluate(X_test, y_test, verbose=verbose)

    score_train = model.evaluate(X_train, y_train, verbose=verbose)

    if (verbose):
        print "\n\n-----"
        print("Accuracy TEST: %.2f%%" % (score_test[1]*100))
        print("Accuracy TRAIN: %.2f%%" % (score_train[1]*100))
        print "-----"

    return model

#
def get_user(id):

    r = requests.get("http://api.soundcloud.com/users/"+str(id)+"?client_id=02gUJC0hH2ct1EGOcYXQIzRFU91c72Ea").json()

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
        "DuplicateWebsite"]

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

    return user

#Neural Network
(X_train,y_train,X_test,y_test) = getBatches(5000,5000,0)
kamala = keras_nn(X_train,y_train,X_test,y_test,verbose=1)

print "Test..."
x = numpy.asarray([get_user(246928450)])  #Not Spam (Random Zombie User)
x2 = numpy.asarray([get_user(4192879)])   #Not Spam (Konukoii)
x3 = numpy.asarray([get_user(246928489)]) #Spam
x4 = numpy.asarray([get_user(41922879)])  #Not Spam (Random Zombie User)
x5 = numpy.asarray([get_user(4360546)])   #Not Spam (Kygo)
kamala.train_on_batch(x5,numpy.asarray([0]))
print kamala.predict_proba(x,verbose = 0)
print kamala.predict_proba(x2,verbose = 0)
print kamala.predict_proba(x3,verbose = 0)
print kamala.predict_proba(x4,verbose = 0)
print kamala.predict_proba(x5,verbose = 0)
embed()


# f = open('kamala.ser','w')
# pickle.dump(kamala,f)
# f.close()

