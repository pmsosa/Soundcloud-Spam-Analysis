import requests
from collections import Counter
import csv
from IPython import embed

def find_websites():
    with open("cs276_NOV06-2pm.csv", 'r') as f:
        reader = csv.reader(f)
        next(reader)

        i=0 
        websites = Counter()
        

        for r in reader:
            
            if ("goo.gl" in r[2]) or ("bit.ly" in r[2]) or ("tinyurl" in r[2]):
                #print r[2]
                try:
                    x = check_website(r[2][2:-1])
                except:
                    continue;
                print x
                websites[x] += 1
        return websites

def check_website(website):
    r = requests.head(website)
    r = r.headers["Location"]
    return r



if __name__ == "__main__":
    web = find_websites()
    embed()
    #goo.gl/7Tskrw+