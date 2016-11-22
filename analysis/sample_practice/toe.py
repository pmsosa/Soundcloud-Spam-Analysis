from IPython import embed

# Load the Pima Indians diabetes dataset from CSV URL
import numpy as np
import pandas as pd
import urllib
import matplotlib
import pylab
import matplotlib.pyplot as plt
from pandas import DataFrame
from sklearn.cluster import KMeans


df = pd.read_csv('users 3.csv')
#df.plot(x='followers_count', y='followings_count', style='o')
# df.plot.scatter(x='followers_count', y='followings_count', s=area, c=colors, alpha=.15)

k=2
# Initialize the model with 2 parameters -- number of clusters and random state.
kmeans_model = KMeans(n_clusters=2, random_state=1)
# Get only the numeric columns from games.
good_columns = df._get_numeric_data()
good_columns = good_columns[['likes_count','followers_count']]
# Fit the model using the good columns.
kmeans_model.fit(good_columns)
colors = ["g.", "r."]
# Get the cluster assignments.
labels = kmeans_model.labels_
centroids = kmeans_model.cluster_centers_
print (centroids)
print (labels)

for i in range(len(good_columns)):
	if i == 10000:
		break
	#print("coordiate", good_columns.iloc[i], labels[i])
	plt.plot(good_columns.iloc[i]['likes_count'], good_columns.iloc[i]['followers_count'], colors[labels[i]])
# separate the data from the target attributes
plt.show()

# Misc code
