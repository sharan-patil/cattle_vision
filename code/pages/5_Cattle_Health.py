import streamlit as st
import random

# cattle weight, temperature sensor data

HEALTH_STATUS = [
    'Healthy',
    'Needs vaccination',
    'At veterinarian'
]

CATTLE_TYPES = [
    'Cow',
    'Pig',
    'Hen',
    'Turkey'
]

CHECKUP_DATES = [
    '09/17/2024',
    '06/01/2024',
    '12/10/2024',
    '07/29/2024'
]

data = {
    'Cattle ID': [i for i in range(1, 16)],
    'Cattle Type': [random.choice(CATTLE_TYPES) for i in range(1, 16)],
    'Health Status': [random.choice(HEALTH_STATUS) for i in range(1, 16)],
    'Next Scheduled Checkup': [random.choice(CHECKUP_DATES) for i in range(1, 16)]
}

bar_data = {
    'Cattle Type': [random.choice(CATTLE_TYPES) for i in range(1, 16)],
    'Health Status': [random.choice(HEALTH_STATUS) for i in range(1, 16)]
}

line_data = {
    'Cattle ID': [i for i in range(1, 16)],
    'Next Scheduled Checkup': [random.choice(CHECKUP_DATES) for i in range(1, 16)]
}

st.title('Cattle Health')
st.subheader('The data')
st.data_editor(data)
st.subheader('Health status')
st.bar_chart(bar_data, x = 'Cattle Type', y = 'Health Status')
st.subheader('Next appointment due')
st.scatter_chart(line_data, x = 'Cattle ID', y = 'Next Scheduled Checkup')
