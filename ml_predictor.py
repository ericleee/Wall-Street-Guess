# ml_predictor.py
# import websocket
import torch
import joblib
from flask import Flask, render_template

# import finnhub
random_forest_model = joblib.load('random_forest_model.pkl') 

def predict(open_price, close_price):
    features = torch.tensor([[open_price, close_price]], dtype=torch.float)

    # Make a prediction using the RandomForestClassifier
    prediction = random_forest_model.predict(features)

    return int(prediction)  # Convert prediction to integer (0 or 1)


app = Flask("testapp")

# Initialize variables to store the latest price and prediction
latest_price = ???  # You need to replace this with the actual value you obtain from the API
latest_prediction = ???  # You need to replace this with the actual value obtained from prediction

@app.route('/')
def index():
    return render_template('index.html', price=latest_price, prediction=latest_prediction)


if __name__ == "__main__":
    app.run(port=5002)
