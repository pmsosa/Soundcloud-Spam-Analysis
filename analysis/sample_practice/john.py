from IPython import embed

# Load the Pima Indians diabetes dataset from CSV URL
import numpy as np
import pandas as pd
import urllib
import matplotlib
import pylab
import matplotlib.pyplot as plt
from profanity import profanity

from pandas import DataFrame

df = pd.read_csv('users 3.csv')
#df.plot(x='followers_count', y='followings_count', style='o')
#df.plot.scatter(x='followers_count', y='followings_count', c='k', alpha=.15)
#df = df[df.website.str.contains('goo.gl')]
df['last_modified'] =  pd.to_datetime(df['last_modified'], format='u\'%Y/%m/%d %H:%M:%S +0000\'')
df['last_modified_int'] = df.last_modified.astype(np.int64)
df.plot.scatter(x='last_modified_int', y='followings_count', c='k', alpha=.15)
plt.show()

#df['last_modified'] = df['last_modified'].map(lambda x: x[2:-7])
# separate the data from the target attributes


