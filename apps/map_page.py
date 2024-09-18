import streamlit as st
import json
import folium
from streamlit_folium import folium_static
from folium.plugins import Fullscreen, MarkerCluster

def app():
    st.title("Interactive Map with Descriptions")
    
    # Author and general information
    st.write(f"""In this demonstration, we utilize a dataset that includes geographic coordinates alongside descriptive information about various locations. Each entry in our dataset comprises the following components:

Location: The name of the place, providing a clear reference to the geographic feature or city.
Latitude: The geographic latitude of the location, allowing us to pinpoint its position on a map.
Longitude: The geographic longitude, complementing the latitude to ensure precise mapping.
Description: A brief narrative that encapsulates the essence of the location, offering context and inviting brief information from the data set.""")

    # Load the JSON data
    try:
        with open('EN.json', 'r', encoding='utf-8') as file:
            data = json.load(file)
    except FileNotFoundError:
        st.error("The file EN.json was not found. Please ensure it is available in the working directory.")
        st.stop()

    # Initialize the base map using OpenStreetMap
    m = folium.Map(location=[42.0, 24.0], zoom_start=5, control_scale=True)

    # Add fullscreen button to the map
    Fullscreen().add_to(m)

    # Add different tile layers from other providers (without attribution for predefined layers)
    folium.TileLayer(
        'openstreetmap', 
        name='OpenStreetMap'  # No need for attribution for predefined layers
    ).add_to(m)

    folium.TileLayer(
        'cartodb positron', 
        name='CartoDB Positron'  # No attribution needed
    ).add_to(m)
    
    folium.TileLayer(
        'cartodb dark_matter', 
        name='CartoDB Dark Matter'  # No attribution needed
    ).add_to(m)

    # Enable marker clustering
    marker_cluster = MarkerCluster().add_to(m)

    # Loop through the data to add markers
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

    # Add layer control (to switch between map styles)
    folium.LayerControl().add_to(m)

    # Render the map in Streamlit
    folium_static(m)

# Call the function to render the app
app()
