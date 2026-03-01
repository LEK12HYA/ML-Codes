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
k_values=range(2,11) #We are calculating K-Means for multiple k values
sil_scores=[]
ch_scores=[]
db_scores=[]
#n_clusters represents the no.of clusters we want,random state is set to 42 so that same clusters are taken everytime but the starting point is always fixed and n_init is set to auto because KMeans will try many initial centroid positions and pick the best one.
for k in k_values:
  kmeans=KMeans(n_clusters=k,random_state=42,n_init="auto")
  kmeans.fit(x_scaled) #it tells KMeans to find the clusters in the data(here it finds 2 clusters)
  labels=kmeans.labels_ #Values 0/1 are assigned for which cluster each house belongs to

  sil_scores.append(silhouette_score(x_scaled,labels))
  ch_scores.append(calinski_harabasz_score(x_scaled,labels))
  db_scores.append(davies_bouldin_score(x_scaled,labels))
plt.figure(figsize=(15,5)) #figure with width=15,height=5
#Plotting Silhouette Score
plt.subplot(1,3,1)  #(1 row,3 columns,1st subplot)
plt.plot(k_values,sil_scores,marker='o') #Subplot shows how Silhouette Score changes as k changes
plt.title("Silhouette Score vs k")
plt.xlabel("Number of clusters (k)")
plt.ylabel("Silhouette Score")
#Plotting Calinski-Harabasz Score
plt.subplot(1,3,2)
plt.plot(k_values,ch_scores,marker='o',color="green")
plt.title("Calinski-Harabasz Score vs k")
plt.xlabel("Number of clusters (k)")
plt.ylabel("CH Score")
#Davies-Bouldin Index
plt.subplot(1,3,3)
plt.plot(k_values,db_scores,marker='o',color="red")
plt.title("Davies-Bouldin Score vs k")
plt.xlabel("Number of clusters (k)")
plt.ylabel("DB Index")
plt.tight_layout()  #Adjusts spacing between subplots so that titles, labels and axes don't overlap
plt.show()   #Displays all three subplots
