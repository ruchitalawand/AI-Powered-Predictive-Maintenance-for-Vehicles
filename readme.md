# AI-Powered Predictive Maintenance for Vehicles

## **Overview**
This project predicts vehicle part failures (e.g., brakes, engine, battery) using historical sensor data and machine learning.

## **Features**
- Train a RandomForest model on vehicle sensor data.
- Expose a REST API using FastAPI for predictions.
- Supports real-time prediction of part failures.

## **Tech Stack**
- Python, Pandas, Scikit-learn
- FastAPI for API deployment
- Joblib for model persistence

## **Setup**
```bash
# Create environment
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
