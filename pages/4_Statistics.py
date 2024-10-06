import streamlit as st
import pandas as pd
import numpy as np

st.title('Analytics')

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
        <center><font size=5>
            Temperature Graph
        </center></font>
    """, unsafe_allow_html=True)
    st.write('')
    data = {
        'Date': ['May 17, 2024', 'May 18, 2024', 'May 19, 2024', 'May 20, 2024', 'May 21, 2024'],
        'Temperature': list(np.random.randint(50, high=80, size=5))
    }
    chart_data = pd.DataFrame(data)
    st.bar_chart(chart_data, x='Date', y='Temperature')

    st.markdown("""
        <center><font size=5>
            Wind Speed
        </center></font>
    """, unsafe_allow_html=True)
    st.write('')
    data = {
        'Date': ['May 17, 2024', 'May 18, 2024', 'May 19, 2024', 'May 20, 2024', 'May 21, 2024'],
        'Wind Speed': list(np.random.randint(0, high=50, size=5))
    }
    chart_data = pd.DataFrame(data)
    st.bar_chart(chart_data, x='Date', y='Wind Speed')

with col2:
    st.markdown("""
        <center><font size=5>
            Humidity
        </center></font>
    """, unsafe_allow_html=True)
    st.write('')
    data = {
        'Date': ['May 17, 2024', 'May 18, 2024', 'May 19, 2024', 'May 20, 2024', 'May 21, 2024'],
        'Humidity': list(np.random.randint(0, high=20, size=5))
    }
    chart_data = pd.DataFrame(data)
    st.bar_chart(chart_data, x='Date', y='Humidity')

    st.markdown("""
        <center><font size=5>
            Pressure
        </center></font>
    """, unsafe_allow_html=True)
    st.write('')
    data = {
        'Date': ['May 17, 2024', 'May 18, 2024', 'May 19, 2024', 'May 20, 2024', 'May 21, 2024'],
        'Pressure': list(np.random.rand(5))
    }
    chart_data = pd.DataFrame(data)
    st.line_chart(chart_data, x='Date', y='Pressure')

selection = st.selectbox('Pick an inventory item to track quantity', ['Milk', 'Eggs', 'Honey', 'Wool', 'Butter'])

st.markdown(f"""
    <center><font size=5>
        {selection}
    </center></font>
""", unsafe_allow_html=True)
st.write('')
data = {
    'Date': ['May 17, 2024', 'May 18, 2024', 'May 19, 2024', 'May 20, 2024', 'May 21, 2024'],
    'Number of Items': list(np.random.rand(5))
}
chart_data = pd.DataFrame(data)
st.line_chart(chart_data, x='Date', y='Number of Items')
