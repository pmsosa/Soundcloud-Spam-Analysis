import csv
import sys
import collections
import hashlib

FIELDS = 'user_id,id,website,myspace_name,last_name,reposts_count,public_favorites_count,followings_count,full_name,city,first_name,track_count,playlist_count,discogs_name,followers_count,online,username,description,subscriptions,kind,last_modified,website_title,permalink_url,likes_count,permalink,country,uri,avatar_url,comments_count,plan'.split(',')


features = ['public_favorites_count','user_id', 'followings_count', 'followers_count', 'likes_count', 'track_count', 'playlist_count', 'id','user_id', 'comments_count']

discrete_features = ['country',  'plan', 'kind']


is_none_features_list = ['description', 'avatar_url', 'first_name', 'last_name', 'city', 'discogs_name']

is_none_features = {'description':'None','avatar_url': 'https://a1.sndcdn.com/images/default_avatar_large.png', 'first_name': 'None', 'last_name': 'None', 'city':'None', 'discogs_name': 'None'}

class User:
    meta = {}

    def __init__(self, user_dict):
        self.user_dict = collections.OrderedDict()
        for feature in features:
            self.user_dict[feature] = user_dict[feature]
        for dfeature in discrete_features:
            if dfeature not in User.meta:
                User.meta[dfeature] = {}
            x = 0 
            if user_dict[dfeature] not in User.meta[dfeature]:
                User.meta[dfeature][user_dict[dfeature]] = len(User.meta[dfeature])
        for dfeature in discrete_features:
            self.user_dict[dfeature] = User.meta[dfeature][user_dict[dfeature]]

        ##Description

        ##Avatar_URL
        self.user_dict["avatar_url"] = User.meta["avatar_url"][user_dict["avatar_url"]]
        print "Avatar_URL",abs(hash(user_dict["avatar_url"])),user_dict["avatar_url"]

        #First Name
        print 

        #Last Name

        #City

        #Discogs_Name

        for is_none_feature in is_none_features_list:
            self.user_dict[is_none_feature] = 0 if user_dict[is_none_feature] == is_none_features[is_none_feature] else 1

    def to_dict(self):
        return self.user_dict

def parse_file(ifile, ofile):
    rdr = csv.DictReader(ifile)
    wtr = csv.DictWriter(ofile, fieldnames = features+discrete_features+is_none_features_list )
    wtr.writeheader()
    users_processed = 0
    for user_dict in rdr:
        users_processed += 1
        print(users_processed)
        u = User(user_dict)
        wtr.writerow(u.to_dict())
    ifile.close()
    ofile.close()


def main(input_file):
    with open(input_file, 'r') as data_file:
        with open('features.txt', 'w') as ofile:
            parse_file(data_file, ofile)





if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Not enough args.")
    else:
        main(sys.argv[1])

    
