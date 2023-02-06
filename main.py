import streamlit as st
import plotly.express as px
from backend import get_data

#title
st.title("Weather Forecast for the Next Few Days")
place = st.text_input("Place: ")
days = st.slider("Forecast Days", min_value=1, max_value=5,
                 help="Select the number of forecasted days")
option = st.selectbox("Select data to view",
                      ("Temperature", "Sky"))
st.subheader(f"{option} for the next {days} days on {place}")


try:
    if place:
        filtered_data = get_data(place, days)

        if option == "Temperature":
        # Create temperature plot
            temperatures = [(dict["main"]["temp"] /10 - 32) * 5/9 for dict in filtered_data]
            dates = [dict["dt_txt"] for dict in filtered_data]
            figure = px.line(x=dates, y=temperatures, labels={"x": "Date", "y":"Temperature(C)"})
            st.plotly_chart(figure)

        if option =="Sky":
            images = {"Clear": "images/clear.png", "Clouds": "images/cloud.png",
                      "Rain": "images/rain.png", "Snow": "images/snow.png"}
            sky_conditions = [dict["weather"][0]["main"] for dict in filtered_data]
            image_paths = [images[condition] for condition in sky_conditions]
            st.image(image_paths, width=115)

except KeyError:
    st.info("Please enter a valid city name.")