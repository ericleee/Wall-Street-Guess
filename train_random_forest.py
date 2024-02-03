# train_random_forest.py

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib

# Pre-Processing
dataset = pd.read_csv('all_stocks_5yr.csv')
print(dataset.head())

# Drop duplicates based on 'Name' column
dataset.drop_duplicates(subset=['Name'], keep='first', inplace=True)

# Create a new column 'movement' with 0 for down and 1 for up
dataset['movement'] = (dataset['close'] > dataset['open']).astype(int)
print(dataset.head())

# Keep only numeric columns
numeric_columns = dataset.select_dtypes(include='number').columns
dataset = dataset[numeric_columns]

# Check for missing values
print(dataset.isnull().sum())

# Impute or drop missing values
# Example: Impute missing values with mean
dataset = dataset.fillna(dataset.mean())

# Keep only the 'open' and 'close' columns as features
features = dataset[['open', 'close']]

# Keep the 'movement' column as the target variable
labels = dataset['movement']

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(features, labels, test_size=0.16, random_state=32)

# Initialize the Random Forest classifier
random_forest_model = RandomForestClassifier(n_estimators=130, random_state=42)

# Train the model
random_forest_model.fit(X_train, y_train)

# Make predictions on the test set
y_pred = random_forest_model.predict(X_test)

# Evaluate the accuracy
accuracy = accuracy_score(y_test, y_pred)
print(f'Accuracy: {accuracy:.2f}')

# Save the trained model
joblib.dump(random_forest_model, 'random_forest_model.pkl')
