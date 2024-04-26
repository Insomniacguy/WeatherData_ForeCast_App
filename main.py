from datetime import date

import streamlit as st
import pandas as pd
import plotly.express as px

# tile is static so we dont need to place it in a variable
st.title("Weather Forecast For the Next Days")
place = st.text_input("Place:")
days = st.slider(label="Forecast Days", min_value=1, max_value=5, help="Select the number of forecasted days")

options = st.selectbox("Select data to view", ("Temperature", "Sky"))
st.subheader(f"{options} for the next {days} days in {place}")


def get_data(days):
    dates = ["2024-04-22", "2024-04-23", "2024-04-24"]
    temps = [4, 6, 10]
    temps = [days * i for i in temps]
    return dates, temps


# returns tuple of lists

# de-extracting the tuple to get lists as separate values.
d, t = get_data(days)

# used list comprehension to modify the existing temp list
# x and y paraneters of line() from plotly.express module expects lists as arguments
fig = px.line(x=d, y=t, labels={"x": "Date", "y": "Temperature (C)"})
st.plotly_chart(fig)
