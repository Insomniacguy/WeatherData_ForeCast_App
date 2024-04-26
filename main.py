import streamlit as st
import pandas as pd

# tile is static so we dont need to place it in a variable
st.title("Weather Forecast For the Next Days")
place = st.text_input("Place:")
Days = st.slider(label="Forecast Days", min_value=1, max_value=5, help="Select the number of forecasted days")
options = st.selectbox("Select data to view", ("Temperature", "Sky"))
st.subheader(f"{options} for the next {Days} days in {place}")

