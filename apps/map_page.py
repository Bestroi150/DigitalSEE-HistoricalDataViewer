import streamlit as st
import json
import folium
from streamlit_folium import folium_static

def app():
    st.title("Map with Descriptions")

    try:
        with open('EN.json', 'r', encoding='utf-8') as file:
            data = json.load(file)
    except FileNotFoundError:
        st.error("The file EN.json was not found. Please ensure it is available in the working directory.")
        st.stop()

    m = folium.Map(location=[42.0, 24.0], zoom_start=5)

    for entry in data:
        site_object = entry['content']['siteObject']
        latitude = site_object['geographicCoordinates'].get('latitude')
        longitude = site_object['geographicCoordinates'].get('longitude')
        description = site_object['description']

        if latitude and longitude:
            latitude, longitude = float(latitude), float(longitude)
            folium.Marker(
                [latitude, longitude],
                popup=description,
                tooltip=f"{site_object['nameSource']} ({site_object['nameContemporary']})"
            ).add_to(m)

    folium_static(m)
