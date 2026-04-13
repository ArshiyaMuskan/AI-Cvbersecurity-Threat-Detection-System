# ======================from flask import Flask, request, jsonify
import joblib
import pandas as pd
import numpy as np
from flask import Flask, request, jsonify


app = Flask(__name__)

# Load model + columns
model = joblib.load("kdd_model.pkl")
model_columns = joblib.load("model_columns.pkl")

@app.route('/')
def home():
    return "KDD Intrusion Detection API is running 🚀"

# 👉 THIS IS WHERE YOU PASTE THE CODE
@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.json['features']

        df = pd.DataFrame([data])
        df = pd.get_dummies(df)
        df = df.reindex(columns=model_columns, fill_value=0)

        prediction = model.predict(df)

        return jsonify({
            "prediction": str(prediction[0])
        })

    except Exception as e:
        return jsonify({"error": str(e)})

# Run server
if __name__ == '__main__':
    app.run(debug=True)


