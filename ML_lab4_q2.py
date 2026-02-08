import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsRegressor

def regression_scores(y_test, y_pred):
    mse = np.mean((y_test - y_pred) ** 2)
    rmse = np.sqrt(mse)
    mape = np.mean(np.abs((y_test - y_pred) / y_test)) * 100
    r2 = 1 - (np.sum((y_test - y_pred) ** 2) /
              np.sum((y_test - np.mean(y_test)) ** 2))
    return mse, rmse, mape, r2

if __name__ == "__main__":

    file_path = "Lab Session Data.xlsx"
    df = pd.read_excel(file_path, sheet_name="IRCTC Stock Price")  
    X = df.drop(columns=['Date', 'Month', 'Day', 'Volume', 'Chg%'])
    y = df['Chg%']
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.3, random_state=42
    )
    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)  
    knn = KNeighborsRegressor(n_neighbors=3)
    knn.fit(X_train, y_train)
    y_pred = knn.predict(X_test)
    print(regression_scores(y_test, y_pred))
