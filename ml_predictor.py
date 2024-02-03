# ml_predictor.py
# import websocket
import torch
import joblib
import requests

# Load the trained model
random_forest_model = joblib.load('random_forest_model.pkl')

# Function to predict using the model
def predict(open_price, close_price):
    features = torch.tensor([[open_price, close_price]], dtype=torch.float)
    prediction = random_forest_model.predict(features)
    return int(prediction)  # Convert prediction to integer (0 or 1)

# Replace with your actual Finnhub API key
finnhub_api_key = 'your_finnhub_api_key'
symbol = 'GOOGL'  # Replace with the desired stock symbol

# Fetch opening and closing prices from Finnhub API
finnhub_url = f'https://finnhub.io/api/v1/quote?symbol={symbol}&token={finnhub_api_key}'
response = requests.get(finnhub_url)
data = response.json()
open_price = data.get('o', 0)  # 'o' represents the open price
close_price = data.get('c', 0)  # 'c' represents the close price


# Predict using the obtained prices
latest_prediction = predict(open_price, close_price)

# Read the HTML file into a list of lines
with open('template/Stats.html', 'r') as file:
    lines = file.readlines()

# Assuming line 58 is at index 57 (lists are zero-indexed)
line_number_to_replace = 59
html_content = f"<p class='center'>The prediction is that the stock will go {'Up' if latest_prediction == 1 else 'Down'}</p>"


# Replace line 58 with the new content
lines[line_number_to_replace - 1] = html_content + "\n"

# Write the modified lines back to the HTML file
with open('template/Stats.html', 'w') as file:
    file.writelines(lines)
