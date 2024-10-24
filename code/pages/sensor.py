import streamlit as st
import pandas as pd
import numpy as np
import random
import time

# Define sensor types
TEMPERATURE_SENSOR = "Temperature"
HUMIDITY_SENSOR = "Humidity"
HEART_RATE_SENSOR = "Heart Rate"
RUMINATION_TIME_SENSOR = "Rumination Time"
LOCATION_SENSOR = "Location"

# Function to simulate sensor data (replace with actual sensor readings)
def get_sensor_data():
    temperature = random.uniform(60, 90)  # Random temperature value between 60 and 90°F
    humidity = random.uniform(30, 70)      # Random humidity value between 30% and 70%
    heart_rate = random.randint(50, 100)    # Random heart rate value between 50 and 100 beats per minute
    rumination_time = random.randint(10, 20)  # Random rumination time value between 10 and 20 minutes
    cattle_location = [round(random.uniform(30.0, 31.0), 6),
                       round(random.uniform(-97.0, -96.0), 6)]  # Simulating GPS coordinates
    return {
        TEMPERATURE_SENSOR: temperature,
        HUMIDITY_SENSOR: humidity,
        HEART_RATE_SENSOR: heart_rate,
        RUMINATION_TIME_SENSOR: rumination_time,
        LOCATION_SENSOR: cattle_location
    }

# Display sensor readings in real-time
st.title('Sensor Data Dashboard')

sensor_data = get_sensor_data()
col1, col2, col3 = st.columns(3)

with col1:
    st.header('Temperature')
    st.metric(label="Temperature (°F)", value=f"{sensor_data[TEMPERATURE_SENSOR]:.2f}")

with col2:
    st.header('Humidity')
    st.metric(label="Humidity (%)", value=f"{sensor_data[HUMIDITY_SENSOR]:.2f}")

with col3:
    st.header('Heart Rate')
    st.metric(label="Heart Rate (bpm)", value=f"{sensor_data[HEART_RATE_SENSOR]}")

st.header('Rumination Time')
st.metric(label="Rumination Time (minutes)", value=f"{sensor_data[RUMINATION_TIME_SENSOR]}")

st.header('Cattle Location')
st.write(f"Latitude: {sensor_data[LOCATION_SENSOR][0]}, Longitude: {sensor_data[LOCATION_SENSOR][1]}")

# Historical sensor data chart
st.subheader("Historical Sensor Data")

# Create random historical data for multiple sensors (adjust time range as needed)
start_date = pd.Timestamp('2024-05-01')
end_date = pd.Timestamp.today()
dates = pd.date_range(start=start_date, end=end_date, freq='H')  # Hourly data

historical_data = pd.DataFrame({
    'Date': dates,
    TEMPERATURE_SENSOR: [random.uniform(60, 90) for _ in range(len(dates))],
    HUMIDITY_SENSOR: [random.uniform(30, 70) for _ in range(len(dates))],
    HEART_RATE_SENSOR: [random.randint(50, 100) for _ in range(len(dates))],
    RUMINATION_TIME_SENSOR: [random.randint(10, 20) for _ in range(len(dates))]
})

# Line charts for temperature, humidity, heart rate, and rumination time
col1, col2 = st.columns(2)

with col1:
    st.line_chart(historical_data.set_index('Date')[TEMPERATURE_SENSOR], use_container_width=True)
    st.line_chart(historical_data.set_index('Date')[HEART_RATE_SENSOR], use_container_width=True)

with col2:
    st.line_chart(historical_data.set_index('Date')[HUMIDITY_SENSOR], use_container_width=True)
    st.line_chart(historical_data.set_index('Date')[RUMINATION_TIME_SENSOR], use_container_width=True)

# Refresh button to re-run the script
st.button("Refresh Data", on_click=lambda: st.experimental_rerun())
