from datetime import date
import streamlit as st
import plotly.express as px
from backend import get_data

# tile is static so we dont need to place it in a variable
st.title("Weather Forecast For the Next Days")
place = st.text_input("Place:")
days = st.slider(label="Forecast Days", min_value=1, max_value=5, help="Select the number of forecasted days")

options = st.selectbox("Select data to view", ("Temperature", "Sky"))
st.subheader(f"{options} for the next {days} days in {place}")

# if place is not an empty string only then call get_data()
if place:
    try:
        filter_data = get_data(place, days)

        # used list comprehension to modify the existing temp list
        # x and y parameters of line() from plotly.express module expects lists as arguments

        #  Get the temperature/sky data
        if options == "Temperature":
            temperatures = [dict['main']['temp'] / 10 for dict in filter_data]
            dates = [dates['dt_txt'] for dates in filter_data]
            fig = px.line(x=dates, y=temperatures, labels={"x": "Date", "y": "Temperature (C)"})
            st.plotly_chart(fig)
        if options == "Sky":
            images = {'Clouds': 'Images/cloud.png', 'Clear': 'Images/clear.png', 'Rain': 'Images/rain.png', 'Snow':
                'Images/snow.png'}
            sky = [dict['weather'][0]['main'] for dict in filter_data]
            print(sky)
            image_paths = []
            for condition in sky:
                image_path = images[condition]
                image_paths.append(image_path)
            print(image_paths)
            st.image(image_paths, width=120)
    except KeyError:
        st.write("That place does not exist")


