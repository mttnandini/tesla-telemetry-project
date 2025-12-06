import streamlit as st
import pandas as pd
import plotly.express as px
import os

# --------------------------------------------------------
# LOAD PROCESSED DATA
# --------------------------------------------------------
data_path = "data/processed/clean_data.csv"

if not os.path.exists(data_path):
    st.error("❌ Clean data file not found. Please run ETL or anomaly model first.")
    st.stop()

df = pd.read_csv(data_path)

# --------------------------------------------------------
# TITLE
# --------------------------------------------------------
st.title("🚗 Tesla Telemetry Dashboard")
st.write("Real-time analytics and monitoring for vehicle safety.")

# --------------------------------------------------------
# SECTION 1 — BASIC STATS
# --------------------------------------------------------
st.subheader("📊 Vehicle Summary Statistics")
st.write(df.describe())

# --------------------------------------------------------
# SECTION 2 — ANOMALY DETECTION
# --------------------------------------------------------
st.subheader("🚨 Anomaly Detection")

if "anomaly" not in df.columns:
    st.warning("⚠️ No anomaly column found. Run the anomaly model first.")
else:
    st.write("### Detected Anomalies (Red = Issue)")

    fig_anom = px.scatter(
        df,
        x="speed",
        y="battery_temp",
        color="anomaly",
        color_continuous_scale=["red", "blue"],
        title="Anomaly Detection Scatter"
    )
    st.plotly_chart(fig_anom)
    st.success("Anomaly results loaded successfully! ✅")

# --------------------------------------------------------------
# SECTION 3 – BATTERY TEMPERATURE FORECASTING
# --------------------------------------------------------------
st.subheader("📉 Battery Temperature Forecasting")

import os

# ALWAYS resolve absolute path to avoid Streamlit path issues
forecast_file = os.path.join(os.path.dirname(__file__), "..", "data", "processed", "forecast_results.csv")
forecast_file = os.path.abspath(forecast_file)

st.write(f"🔎 Looking for file at: `{forecast_file}`")

if os.path.exists(forecast_file):
    forecast_df = pd.read_csv(forecast_file)

    st.success("Forecasting results loaded successfully! 🚀")
    st.write("### Forecast Data Preview")
    st.dataframe(forecast_df.head())

    # Create forecast line chart
    fig_forecast = px.line(
        forecast_df,
        x="timestamp",
        y="forecast_battery_temp",
        title="Battery Temperature Forecast"
    )
    st.plotly_chart(fig_forecast)

else:
    st.error("❌ Forecast file NOT FOUND. Please run forecasting_models.py again.")


