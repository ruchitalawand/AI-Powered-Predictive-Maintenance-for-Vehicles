import joblib
import numpy as np
import os

def predict_failure(features):
    """
    features = [engine_temp, battery_voltage, oil_pressure, brake_wear, engine_hours]
    """
    model_path = os.path.join('models', 'predictive_model.pkl')
    model = joblib.load(model_path)
    prediction = model.predict([features])
    return prediction[0]

if __name__ == "__main__":
    sample_input = [105, 11.7, 28, 48, 2200]
    result = predict_failure(sample_input)
    print("Part Failure Prediction:", "YES" if result == 1 else "NO")
