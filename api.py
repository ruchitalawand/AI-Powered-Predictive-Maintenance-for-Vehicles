from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
from predict import predict_failure

app = FastAPI(title="Predictive Maintenance API")

class VehicleData(BaseModel):
    engine_temp: float
    battery_voltage: float
    oil_pressure: float
    brake_wear: float
    engine_hours: int

@app.post("/predict")
def get_prediction(data: VehicleData):
    features = [
        data.engine_temp,
        data.battery_voltage,
        data.oil_pressure,
        data.brake_wear,
        data.engine_hours
    ]
    prediction = predict_failure(features)
    return {"part_failure": bool(prediction)}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
