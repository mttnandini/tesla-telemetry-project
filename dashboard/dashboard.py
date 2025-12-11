import streamlit as st
import pandas as pd
import plotly.express as px
import os

# --------------------------------------------------------
# FIXED FILE PATHS (WORKS LOCALLY + STREAMLIT CLOUD)
# --------------------------------------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DATA_PATH = os.path.abspath(os.path.join(BASE_DIR, "..", "data", "processed", "clean_data.csv"))
FORECAST_PATH = os.path.abspath(os.path.join(BASE_DIR, "..", "data", "processed", "forecast_results.csv"))

# --------------------------------------------------------
# LOAD DATA
# --------------------------------------------------------
if not os.path.exists(DATA_PATH):
    st.error("❌ clean_data.csv NOT FOUND. Make sure the file is inside data/processed/")
    st.stop()

df = pd.read_csv(DATA_PATH)

# --------------------------------------------------------
# TITLE
# --------------------------------------------------------
st.title("🚗 Tesla Telemetry Dashboard")
st.write("Real-time vehicle monitoring • anomaly detection • forecasting")

# --------------------------------------------------------
# SECTION 1 — SUMMARY STATISTICS
# --------------------------------------------------------
st.subheader("📊 Vehicle Summary Statistics")
st.write(df.describe())

# --------------------------------------------------------
# SECTION 2 — ANOMALY VISUALIZATION
# --------------------------------------------------------
st.subheader("🚨 Anomaly Detection")

if "anomaly" in df.columns:
    fig_anom = px.scatter(
        df,
        x="speed",
        y="battery_temp",
        color="anomaly",
        color_continuous_scale=["red", "blue"],
        title="Anomaly Detection Scatter"
    )
    st.plotly_chart(fig_anom)
else:
    st.warning("⚠️ No anomaly column found. Run anomaly model first.")

# --------------------------------------------------------
# SECTION 3 — FORECASTING
# --------------------------------------------------------
st.subheader("📉 Battery Temperature Forecast")

if os.path.exists(FORECAST_PATH):
    forecast_df = pd.read_csv(FORECAST_PATH)
    st.write(forecast_df.head())

    fig_fc = px.line(
        forecast_df,
        x="timestamp",
        y="forecast_battery_temp",
        title="Battery Temperature Forecast"
    )
    st.plotly_chart(fig_fc)
else:
    st.error("❌ forecast_results.csv NOT FOUND. Run forecasting model again.")

# --------------------------------------------------------
# SECTION 4 — USER INPUT SAFETY CHECK
# --------------------------------------------------------
st.subheader("🛠️ Try Your Own Input Values")

speed = st.slider("Speed (km/h)", 0, 200, 50)
battery = st.slider("Battery Temp (°C)", 0, 120, 40)
motor = st.slider("Motor Temp (°C)", 0, 200, 90)

if st.button("Run Safety Check"):
    if battery > 80 or motor > 140:
        st.error("⚠️ Warning: Unsafe Operation Detected!")
    else:
        st.success("✔️ Normal — Safe Operation")
