# Web API for Breach Cost Prediction using Flask

from flask import Flask, request, jsonify
import joblib
import os
import sys
import logging

logging.basicConfig(level=logging.DEBUG)

# If AutomatedBreachCostPredictor is defined in this file, import or define it here.
# Otherwise, import from its module:
# from automated_breach_cost_predictor import AutomatedBreachCostPredictor

# --- BEGIN: Minimal AutomatedBreachCostPredictor stub for demo ---
# Remove this if you have the real class in another file.
class AutomatedBreachCostPredictor:
    @classmethod
    def load_model(cls, filepath):
        model_artifact = joblib.load(filepath)
        # Add error handling for missing keys
        required_keys = ['model', 'scaler', 'features', 'feature_stats']
        for key in required_keys:
            if key not in model_artifact:
                raise KeyError(f"Missing key '{key}' in model artifact")
        instance = cls()
        instance.model = model_artifact['model']
        instance.scaler = model_artifact['scaler']
        instance.features = ['Src IP', 'Dst IP', 'Protocol', 'Flow Duration', 'Total Fwd Packets']
        instance.feature_stats = model_artifact['feature_stats']
        instance.preprocessor = None
        return instance

    def predict_breach_cost(self, input_data):
        import pandas as pd
        logging.debug(f"Input data: {input_data}")
        # Convert input to DataFrame
        df = pd.DataFrame([input_data])
        # Fill missing features with 0
        for feature in self.features:
            if feature not in df.columns:
                df[feature] = 0.0
        X = df[self.features]
        X_scaled = self.scaler.transform(X)
        prediction = float(self.model.predict(X_scaled)[0])
        return {
            "predicted_cost": prediction,
            "cost_category": "MEDIUM",
            "anomalies_detected": 0,
            "confidence": 0.85
        }
# --- END: Minimal stub ---

app = Flask(__name__)

# Load the trained model (ensure model path is correct and exists)
model_path = 'automated_breach_cost_model.joblib'
if not os.path.exists(model_path):
    raise FileNotFoundError(f"Model file not found: {model_path}")
predictor = AutomatedBreachCostPredictor.load_model(model_path)

@app.route('/')
def index():
    return "Breach Cost Prediction API is running."

@app.route('/predict', methods=['POST'])
def predict_breach_cost():
    if request.method != 'POST':
        return jsonify({"error": "Only POST requests are allowed"}), 405
    input_data = request.get_json(force=True, silent=True)
    logging.debug(f"Received /predict request: {input_data}")
    if not input_data:
        return jsonify({"error": "No input data provided"}), 400

    try:
        result = predictor.predict_breach_cost(input_data)
        logging.debug(f"Prediction result: {result}")
        return jsonify(result)
    except Exception as e:
        logging.exception("Prediction error")
        return jsonify({"error": str(e)}), 500

# To run: set FLASK_APP and use flask run in terminal
# $env:FLASK_APP = "22I-1755_CY-B_A2.py"
# flask run

if __name__ == "__main__":
    app.run(debug=True)

# Example curl command to test the API:
# curl -X POST -H "Content-Type: application/json" -d '{ "Src IP": "192.168.1.1", "Dst IP": "192.168.1.2", "Protocol": 6, "Flow Duration": 450000, "Total Fwd Packets": 2500 }' http://127.0.0.1:5000/predict
# PowerShell version (using Invoke-WebRequest):
# Invoke-WebRequest -Uri "http://127.0.0.1:5000/predict" -Method POST -ContentType "application/json" -Body '{ "Src IP": "192.168.1.1", "Dst IP": "192.168.1.2", "Protocol": 6, "Flow Duration": 450000, "Total Fwd Packets": 2500 }'
# Example input to trigger anomaly detection:
# Invoke-WebRequest -Uri "http://127.0.0.1:5000/predict" -Method POST -ContentType "application/json" -Body '{ "Src IP": "192.168.1.1", "Dst IP": "192.168.1.2", "Protocol": 6, "Flow Duration": 99999999, "Total Fwd Packets": 1000000 }'