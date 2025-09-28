# Cybersecurity Breach Cost Prediction API

A complete machine learning pipeline and RESTful API for predicting the financial impact of cybersecurity breaches using network traffic data.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [API Reference](#api-reference)
- [Example Request](#example-request)
- [Anomaly Detection](#anomaly-detection)
- [Project Structure](#project-structure)
- [License](#license)
- [Contact](#contact)

## Overview

This project enables organizations to estimate breach costs and detect anomalies in network traffic using a trained ML model. It combines data science and cybersecurity for actionable insights.

## Features

- Data preprocessing and feature engineering
- Automated model training and evaluation
- Anomaly detection using statistical methods
- Flask-based REST API for real-time predictions
- PDF report generation (Jupyter notebook)
- Model deployment and monitoring scripts

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/ibrahim-khan12/breach-cost-prediction-api.git
   cd breach-cost-prediction-api
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Train the Model

You can train the model using the provided Jupyter notebook or Python scripts.  
A pre-trained model file (`automated_breach_cost_model.joblib`) is included for quick API setup.

### Run the API

Set the Flask app and start the server:

**PowerShell**
```powershell
$env:FLASK_APP = "22I-1755_CY-B_A2.py"
flask run
```

**Command Prompt**
```cmd
set FLASK_APP=22I-1755_CY-B_A2.py
flask run
```

## API Reference

### Endpoint

`POST /predict`

### Request Body

Send a JSON object with network traffic features.  
**Example:**
```json
{
  "Src IP": "192.168.1.1",
  "Dst IP": "192.168.1.2",
  "Protocol": 6,
  "Flow Duration": 450000,
  "Total Fwd Packets": 2500
}
```

### Response

```json
{
  "predicted_cost": 18750.23,
  "cost_category": "MEDIUM",
  "anomalies_detected": 0,
  "confidence": 0.85
}
```

## Example Request

**PowerShell**
```powershell
Invoke-WebRequest -Uri "http://127.0.0.1:5000/predict" -Method POST -ContentType "application/json" -Body '{ "Src IP": "192.168.1.1", "Dst IP": "192.168.1.2", "Protocol": 6, "Flow Duration": 450000, "Total Fwd Packets": 2500 }'
```

**Command Prompt**
```cmd
curl -X POST -H "Content-Type: application/json" -d "{\"Src IP\": \"192.168.1.1\", \"Dst IP\": \"192.168.1.2\", \"Protocol\": 6, \"Flow Duration\": 450000, \"Total Fwd Packets\": 2500}" http://127.0.0.1:5000/predict
```

## Anomaly Detection

To trigger anomaly detection, use extreme values:
```powershell
Invoke-WebRequest -Uri "http://127.0.0.1:5000/predict" -Method POST -ContentType "application/json" -Body '{ "Src IP": "192.168.1.1", "Dst IP": "192.168.1.2", "Protocol": 6, "Flow Duration": 99999999, "Total Fwd Packets": 1000000 }'
```

## Project Structure

```
├── 22I-1755_CY-B_A2.py           # Flask API and model logic
├── 22I-1755_CY-B_A2.ipynb        # Jupyter notebook for analysis/report
├── automated_breach_cost_model.joblib # Trained model file
├── requirements.txt              # Python dependencies
├── README.md                     # Project documentation
├── linkedin_post.md              # Sample LinkedIn post
└── ...                           # Other scripts and files
```

## License

This project is licensed under the MIT License.

## Contact

For questions or feedback, open an issue or connect on [LinkedIn](https://www.linkedin.com/).

---
*Built by Muhammad ibrahim*
