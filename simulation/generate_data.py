# I am importing the random module to generate random values
import random

# I am importing json to save my generated telemetry data in a JSON file
import json

# I am importing datetime to add a timestamp for each generated data record
from datetime import datetime

# This variable stores where I want my generated data file to be saved
# I am saving it in data/raw so that my project stays organized
OUTPUT_FILE = "data/raw/telemetry_data.json"


# This function creates ONE fake telemetry record for a Tesla-like vehicle
def generate_record():
    # I am returning a dictionary because each telemetry row is key-value format
    return {
        "vehicle_id": "EV001",  # static ID just to identify the vehicle
        "speed": round(random.uniform(20, 100), 2),  # random driving speed
        "battery_temp": round(random.uniform(25, 45), 2),  # battery temperature in °C
        "motor_torque": round(random.uniform(100, 300), 2),  # torque in Nm
        "energy_consumption": round(random.uniform(8, 20), 2),  # kWh usage
        "outside_temp": round(random.uniform(10, 35), 2),  # outside weather temperature
        # I am adding a timestamp to show when this record was “generated”
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }


# This function generates MANY telemetry records and saves them into one file
def generate_dataset(n_records=200):
    # I am using list comprehension to create a list of fake records
    data = [generate_record() for _ in range(n_records)]

    # I am opening the output file in write mode to save my generated dataset
    with open(OUTPUT_FILE, "w") as f:
        # I am using json.dump to write the data into the file with indentation for readability
        json.dump(data, f, indent=4)

    # This print statement helps me confirm the data was successfully created
    print(f"✔ Generated {n_records} records at {OUTPUT_FILE}")


# This ensures that the dataset is only generated when I run this file directly
# not when it is imported somewhere else
if __name__ == "__main__":
    generate_dataset()

