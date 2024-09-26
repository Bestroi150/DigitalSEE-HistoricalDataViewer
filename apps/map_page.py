import streamlit as st
import json
import folium
from streamlit_folium import folium_static
from folium.plugins import Fullscreen, MarkerCluster
import requests

def app():
    st.title("Interactive Map with Descriptions")
    

    st.write(f"""In this demonstration, we utilize a dataset that includes geographic coordinates alongside descriptive information about various locations. Each entry in our dataset comprises the following components:
The map can be expandanded and it's layers can be changed. We utilize a OpenStreetMap and CartoDB(Light and Dark Mode).
Location: The name of the place, providing a clear reference to the geographic feature or city.
Latitude: The geographic latitude of the location, allowing us to pinpoint its position on a map.
Longitude: The geographic longitude, complementing the latitude to ensure precise mapping.
Description: A brief narrative that encapsulates the essence of the location, offering context and inviting brief information from the data set.
This demonstration shows the potential of the dataset at hand to be used in a GIS-based software suitable for Digital Archaeology research""")

    try:
        url = 'https://raw.githubusercontent.com/Bestroi150/DigitalSEE/main/JSON/EN.json'
        response = requests.get(url)
        response.raise_for_status()  
        data = response.json()
    except requests.exceptions.RequestException as e:
        st.error(f"An error occurred while fetching the file: {e}")
        st.stop()

   
    m = folium.Map(location=[42.0, 24.0], zoom_start=5, control_scale=True)

   
    Fullscreen().add_to(m)

    folium.TileLayer(
        'openstreetmap', 
        name='OpenStreetMap' 
    ).add_to(m)

    folium.TileLayer(
        'cartodb positron', 
        name='CartoDB Positron'  
    ).add_to(m)
    
    marker_cluster = MarkerCluster().add_to(m)

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
            ).add_to(marker_cluster)  # Add markers to the cluster

    folium.LayerControl().add_to(m)

    folium_static(m)

app()
