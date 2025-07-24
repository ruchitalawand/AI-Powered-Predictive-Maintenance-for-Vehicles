# AI-Powered-Predictive-Maintenance-for-Vehicles
Developed an AI-powered predictive maintenance system for vehicles that analyzes real-time sensor data like engine temperature, oil pressure, and battery voltage to forecast component failures. Built with Python, Scikit-learn, and FastAPI, it provides real-time predictions via a REST API, helping reduce downtime and optimize maintenance schedules.
# Key Features
Data Collection & Preprocessing:
Uses historical sensor data such as engine temperature, oil pressure, battery voltage, brake wear, and engine hours.
Handles missing data and outliers with data-cleaning pipelines.
Machine Learning Model:
A Random Forest Classifier predicts whether a vehicle component is likely to fail soon.
Hyperparameter tuning ensures optimal performance.
REST API Integration:
A FastAPI-based REST service exposes a /predict endpoint for real-time predictions.
Users can send sensor readings (JSON format) and receive a failure probability.
Deployment Ready:
Packaged with requirements.txt and can be containerized with Docker.
Designed for integration with vehicle management dashboards or IoT systems.
Analytics Dashboard (Optional Extension):
Visualizes failure probabilities and maintenance trends using Grafana/Streamlit.

# Tech Stack
Programming Language: Python 3.x
Machine Learning: Scikit-learn, Pandas, NumPy
API Development: FastAPI, Uvicorn
Model Persistence: Joblib
Version Control & Deployment: Git, Docker (optional)

# Workflow
Data Input: Vehicle sensor readings (temperature, oil pressure, brake wear, etc.).
Model Training: The model learns from historical failure data to predict future failures.
Prediction API: The API receives data and predicts component failure (YES/NO).
Maintenance Insights: Helps schedule preventive maintenance actions.

# Use Cases
Automobile Industry:
Fleet operators can schedule maintenance before failures occur, improving vehicle uptime.
OEMs & Dealerships:
Provide predictive maintenance as a value-added service.
Smart IoT Systems:
Integrate with vehicle telematics for real-time health monitoring.
Impact
Reduces downtime by predicting failures early.
Improves cost efficiency for fleet management.
Enhances customer satisfaction with proactive service.
