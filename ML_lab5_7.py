import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score,calinski_harabasz_score,davies_bouldin_score
import matplotlib.pyplot as plt
df=pd.read_csv("housing.csv")   #Reads a CSV file into a dataframe which is like a table
##This is to fill the missing values in numeric columns with median
numeric_cols=["longitude","latitude","housing_median_age","total_rooms","total_bedrooms","population","households","median_income"]
df[numeric_cols]=df[numeric_cols].fillna(df[numeric_cols].median())
#For each category in ocean_proximity it creates a neaw column that has 0/1 label and later with drp first=True it removes the first category to remove any confusion/errors.
x_train=pd.get_dummies(df[["longitude","latitude","housing_median_age","total_rooms","total_bedrooms","population","households","median_income","ocean_proximity"]],drop_first=True) #x_train here represents the features that are used to predict
                                #[[]] are used so that we can put it in the form of dataform instead of series and it is taken as 2D because sci-kit learn expects many inputs
scaler=StandardScaler()  # It is used to standardize the features so that they have mean=0 and std=1 so when calculating distances b/w pts in KMeans larger features don't dominate the distance calculation.
x_scaled=scaler.fit_transform(x_train) #Computes the mean & std of each feature which transforms each value to (value-mean)/std
distortions=[]
k_values=range(2,20) #As we want to test on different k values we have taken accordingly and as we want meaningful clusters we have taken from 2
for k in k_values:
    kmeans=KMeans(n_clusters=k,random_state=42,n_init="auto")
    kmeans.fit(x_scaled)
    distortions.append(kmeans.inertia_) #the sum of squared distances from each data point to its assigned cluster center.(Lower=closer to cluster centers and clusters are tight)
#Appending it to distortions builds a list of inertia values for each k
plt.figure(figsize=(8,5))
plt.plot(k_values,distortions,marker="o")
plt.xlabel("Number of clusters (k)")
plt.ylabel("Distortion")
plt.title("Elbow Method for optimal k")
plt.show()
