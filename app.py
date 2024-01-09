import pickle
from flask import Flask, request, jsonify
import numpy as np
import pandas as pd

from sklearn.preprocessing import StandardScaler
from src.pipeline.predict_pipeline import CustomData, PredictPipeline

app = Flask(__name__)

@app.route("/")
def home():
    return "<h3>Sklearn Prediction for Student Score Prediction</h3>"

@app.route("/predict", methods=["POST"])
def predict():

    inference_payload = pd.DataFrame(request.json)

    print(inference_payload)

    request_df = pd.DataFrame()

    predict_pipeline = PredictPipeline()
    prediction = predict_pipeline.predict(request_df)

    return jsonify({'prediction': prediction})


if __name__ == "__main__":

    app.run(host='0.0.0.0', debug=True)
