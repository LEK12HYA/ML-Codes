import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
df = pd.read_csv("Feature_data.csv")
df = df[df["label"].isin([0, 1])]
feature_cols = [col for col in df.columns if col.startswith("F")]

X = df[feature_cols].values   # Feature matrix
y = df["label"].values     
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.3,
    stratify=y,
    random_state=42
)

print("Training samples:", X_train.shape)
print("Testing samples:", X_test.shape)
# A7: Train kNN Classifier (k = 3)

neigh = KNeighborsClassifier(n_neighbors=3)
neigh.fit(X_train, y_train)

print("\n kNN model trained with k = 3")
# Test Accuracy on Test Set
accuracy = neigh.score(X_test, y_test)
print("\n Test Accuracy:", accuracy)
# A9: Predict Class Labels for Test Data
y_pred = neigh.predict(X_test)

print("\n Predicted labels (first 10):", y_pred[:10])
print(" Actual labels    (first 10):", y_test[:10])
test_vect = X_test[0].reshape(1, -1)
predicted_class = neigh.predict(test_vect)

print("\n Prediction for one test vector:", predicted_class)
