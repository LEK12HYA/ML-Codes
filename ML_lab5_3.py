import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression      #LinearRegression model finds a straight line that best fits the data
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error,r2_score,mean_absolute_percentage_error
df=pd.read_csv("housing.csv")   #Reads a CSV file into a dataframe which is like a table
##This is to fill the missing values in numeric columns with median
numeric_cols=["longitude","latitude","housing_median_age","total_rooms","total_bedrooms","population","households","median_income"]
df[numeric_cols]=df[numeric_cols].fillna(df[numeric_cols].median())
#For each category in ocean_proximity it creates a neaw column that has 0/1 label and later with drp first=True it removes the first category to remove any confusion/errors.
x_train=pd.get_dummies(df[["longitude","latitude","housing_median_age","total_rooms","total_bedrooms","population","households","median_income","ocean_proximity"]],drop_first=True)   #x_train here represents the features that are used to predict
                                #[[]] are used so that we can put it in the form of dataform instead of series and it is taken as 2D because sci-kit learn expects many inputs
y_train=df["median_house_value"] #the target can be 1D because it gives singe value per sample
x_train,x_test,y_train,y_test=train_test_split(x_train,y_train,test_size=0.2,random_state=42)  #This helps in splitting the data into training and testing sets
                             #test size here shows that only 20% of the data will be going for testing and 80% will be used for training
                            #We split the model into training and testing to see how well the model works on unseen data
                            #x_train and y_train represent the data that is used to train the model and x_test and y_test is the data to check how well the model works for unseen data                                                                              
reg=LinearRegression()      #from ski-kit we import LinearRegression model and store it in the variable reg which is empty as it did not learn anything
fit_data=reg.fit(x_train,y_train)    #.fit() helps to teach the model the relationship between x and y from the traing data
                                     #it calculates the slope and intercept so that it can reduce the difference between the predicted and the actual value.
y_test_pred=reg.predict(x_test)     #.predict() uses the trained model to predict the output for x_test
y_train_pred=reg.predict(x_train)   #Predicted values for the trainig set
##A2.
def calculate_metrics(y_true,y_pred):  #y_true is the actual values and y_pred is the predicted values
    mse=mean_squared_error(y_true,y_pred)  #Mean Square Error. It tells how far is actual value from the predicted values. It is in squared values
    rmse=np.sqrt(mse) #Root Mean Square Error. It converts the squared units of MSE to RMSE
    mape=mean_absolute_percentage_error(y_true,y_pred) #Mean Absolute Percentage Error. It gives the error in the form of percentage.
    r2=r2_score(y_true,y_pred) #R2 Score. It tells how well the model explains the variation in the target using the features.
    metrics={"MSE":mse,"RMSE":rmse,"MAPE":mape,"R2":r2} #Stores all four metrices in a dictionary so that they are easy to access
    return metrics
train_metrics=calculate_metrics(y_train,y_train_pred) #Tells how well the model works for training data inorder to see how well the model learned the training data
test_metrics=calculate_metrics(y_test,y_test_pred) #Tells how well the model works for testing data
print("First 5 predictions:",y_test_pred[:5]) #Shows the first 5 predictions of the model
print("Slope:",reg.coef_)   #Slope tells how much house value changes with income
print("Intercept:",reg.intercept_)  #Intercept tells us where the line starts on the y-axis(if the income=0 then the value of the house)
print("Train Metrics:",train_metrics)
print("Test Metrics:",test_metrics)
