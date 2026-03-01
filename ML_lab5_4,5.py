import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score,calinski_harabasz_score,davies_bouldin_score
df=pd.read_csv("housing.csv")   #Reads a CSV file into a dataframe which is like a table
##This is to fill the missing values in numeric columns with median
numeric_cols=["longitude","latitude","housing_median_age","total_rooms","total_bedrooms","population","households","median_income"]
df[numeric_cols]=df[numeric_cols].fillna(df[numeric_cols].median())
#For each category in ocean_proximity it creates a neaw column that has 0/1 label and later with drp first=True it removes the first category to remove any confusion/errors.
x_train=pd.get_dummies(df[["longitude","latitude","housing_median_age","total_rooms","total_bedrooms","population","households","median_income","ocean_proximity"]],drop_first=True) #x_train here represents the features that are used to predict
                                #[[]] are used so that we can put it in the form of dataform instead of series and it is taken as 2D because sci-kit learn expects many inputs
scaler=StandardScaler()  # It is used to standardize the features so that they have mean=0 and std=1 so when calculating distances b/w pts in KMeans larger features don't dominate the distance calculation.
x_scaled=scaler.fit_transform(x_train) #Computes the mean & std of each feature which transforms each value to (value-mean)/std
#n_clusters represents the no.of clusters we want,random state is set to 0 so that same clusters are taken everytime but the starting point is choosen in random and n_init is set to auto because KMeans will try many initial centroid positions and pick the best one.
kmeans=KMeans(n_clusters=2,random_state=0,n_init="auto")
kmeans.fit(x_scaled) #it tells KMeans to find the clusters in the data(here it finds 2 clusters)
labels=kmeans.labels_ #Values 0/1 are assigned for which cluster each house belongs to
centers=kmeans.cluster_centers_ #Represents the average house in each cluster
unique,counts=np.unique(labels,return_counts=True)  #Helps in finding unique cluste labels and also how many points are in each cluster
cluster_distribution=dict(zip(unique,counts)) #Creates a dictionary showing cluster sizes.
print("Cluster labels for the first 10 houses:",labels[:10])
print("Cluster centers:",centers)
print("Number of houses in each cluster:",cluster_distribution)
#x_scaled is taken so that all features contribute fairly when KMeans calculates distances and cluster points
sil_score=silhouette_score(x_scaled,labels) #Tells us how well each house fits in its cluster
ch_score=calinski_harabasz_score(x_scaled,labels) # It sees how far apart the clusters are compared to how tight they are
db_index=davies_bouldin_score(x_scaled,labels)  #Measures how similar each cluster is to others
print("Clustering Evaluation Metrics:")
print("Silhouette Score:",sil_score)
print("Calinski-Harabasz Score:",ch_score)
print("Davies-Bouldin Index:",db_index)
