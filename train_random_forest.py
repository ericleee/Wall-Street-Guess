# train_random_forest.py

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib

dataset = pd.read_csv('all_stocks_5yr.csv')

features = dataset.drop('close', axis=1)
labels = dataset['close']

# Keep only the 'open' and 'close' columns as features
features = dataset[['open', 'close']]

# Keep the 'label' column as the target variable
labels = dataset['close']
# Check for missing values
print(dataset.isnull().sum())

# Impute or drop missing values
# Example: Impute missing values with mean
data = dataset.fillna(dataset.mean())

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(features, labels, test_size=0.2, random_state=42)


# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(features, labels, test_size=0.2, random_state=42)

# Initialize the Random Forest classifier
random_forest_model = RandomForestClassifier(n_estimators=100, random_state=42)

# Train the model
random_forest_model.fit(X_train, y_train)

# Make predictions on the test set
y_pred = random_forest_model.predict(X_test)

# Evaluate the accuracy
accuracy = accuracy_score(y_test, y_pred)
print(f'Accuracy: {accuracy:.2f}')

joblib.dump(random_forest_model, 'random_forest_model.pkl')

