import pandas as pd
from sklearn.linear_model import LinearRegression

# Load clean data
df = pd.read_csv("data/processed/clean_data.csv")

# Simple model: battery temperature vs speed (placeholder model)
X = df[["speed"]]
y = df["battery_temp"]

model = LinearRegression()
model.fit(X, y)

# Predict
df["forecast_battery_temp"] = model.predict(X)

# Save output
df[["timestamp", "forecast_battery_temp"]].to_csv(
    "data/processed/forecast_results.csv",
    index=False
)

print("Forecasting model complete. Predictions saved!")
