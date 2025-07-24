import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib
import os

# Load data
data_path = os.path.join('data', 'vehicle_data.csv')
df = pd.read_csv(data_path)

X = df.drop('part_failure', axis=1)
y = df['part_failure']

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Save model
os.makedirs('models', exist_ok=True)
joblib.dump(model, os.path.join('models', 'predictive_model.pkl'))

print("Model trained and saved!")
