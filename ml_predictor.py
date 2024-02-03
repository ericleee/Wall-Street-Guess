# ml_module.py
import json
import websocket
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


app = Flask(__name__)

# Initialize variables to store the latest price and prediction
latest_price = None
latest_prediction = None

@app.route('/')
def home():
    return render_template('index.html', price=latest_price, prediction=latest_prediction)

def on_message(ws, message):
    global latest_price, latest_prediction

    data = json.loads(message)
    if 'data' in data and isinstance(data['data'], list):
        for item in data['data']:
            if 'p' in item:
                price = item['p']
                open_price = price 
                close_price = price 

                prediction = predict(open_price, close_price)

                print(f"Received Price: {price}, Prediction: {'Up' if prediction == 1 else 'Down'}")

                # Update the latest price and prediction
                latest_price = price
                latest_prediction = prediction

                # Now, you can pass the received data to your HTML template
                return render_template('index.html', price=latest_price, prediction=latest_prediction)

def on_error(ws, error):
    print(error)

def on_close(ws):
    print("### closed ###")

def on_open(ws):
    ws.send('{"type":"subscribe","symbol":"BINANCE:BTCUSDT"}')
    ws.send('{"type":"subscribe","symbol":"IC MARKETS:1"}')

if __name__ == "__main__":
    websocket.enableTrace(True)
    ws = websocket.WebSocketApp("wss://ws.finnhub.io?token=cmv7nh1r01qog1iuhbqgcmv7nh1r01qog1iuhbr0",
                              on_message=on_message,
                              on_error=on_error,
                              on_close=on_close)
    ws.on_open = on_open
    ws.run_forever()