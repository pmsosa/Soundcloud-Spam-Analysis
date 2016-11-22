from IPython import embed

# Load the Pima Indians diabetes dataset from CSV URL
import numpy as np
import pandas as pd
import urllib
import matplotlib
import pylab
import matplotlib.pyplot as plt
from pandas import DataFrame

df = pd.read_csv('users 3.csv')
embed()
#df.plot(x='followers_count', y='followings_count', style='o')
df.plot.scatter(x='followers_count', y='followings_count', c='k', alpha=.15)
plt.xlim(0, 100)
plt.ylim(150, 350)
plt.show()

# separate the data from the target attributes

# Misc code
