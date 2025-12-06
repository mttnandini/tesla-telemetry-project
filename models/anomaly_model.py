import pandas as pd
from sklearn.ensemble import IsolationForest

# 1. Load clean data
df = pd.read_csv("data/processed/clean_data.csv")

# 2. Train anomaly model
model = IsolationForest(contamination=0.03, random_state=42)
df["anomaly"] = model.fit_predict(df[["battery_temp", "motor_torque", "energy_consumption"]])

# Convert anomaly label: -1 = anomaly → 1, 1 = normal → 0
df["anomaly"] = df["anomaly"].map({1: 0, -1: 1})

# 3. Save updated dataframe
df.to_csv("data/processed/clean_data.csv", index=False)

print("Anomaly detection complete. Updated file saved!")
