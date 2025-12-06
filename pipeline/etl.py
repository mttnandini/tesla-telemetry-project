# Importing necessary libraries
import json
import pandas as pd

# Function to load the raw telemetry data
def load_raw_data(filepath="data/raw/telemetry_data.json"):
    print("➡ Loading raw data...")
    with open(filepath, "r") as f:
        data = json.load(f)
    print("✔ Raw data loaded successfully!")
    return data

# Function to clean and transform the raw data
def clean_data(data):
    print("➡ Cleaning data...")
    df = pd.DataFrame(data)

    # Converting timestamp column to datetime
    df["timestamp"] = pd.to_datetime(df["timestamp"])

    # Sorting by time
    df = df.sort_values("timestamp")

    # Resetting index after sorting
    df.reset_index(drop=True, inplace=True)

    # Adding a new feature: difference between battery temp and outside temp
    df["temp_difference"] = df["battery_temp"] - df["outside_temp"]

    print("✔ Data cleaned successfully!")
    return df

# Function to save cleaned data
def save_processed_data(df, output_path="data/processed/clean_data.csv"):
    print(f"➡ Saving cleaned data to {output_path}...")
    df.to_csv(output_path, index=False)
    print("✔ Cleaned data saved successfully!")

# Main ETL pipeline
def run_etl():
    print("\n🚀 Starting ETL pipeline...\n")

    raw_data = load_raw_data()
    cleaned_df = clean_data(raw_data)
    save_processed_data(cleaned_df)

    print("\n🎉 ETL pipeline completed successfully!\n")

# Making sure ETL runs only when this file is executed directly
if __name__ == "__main__":
    run_etl()

