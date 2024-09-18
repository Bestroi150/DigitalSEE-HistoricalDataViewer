import streamlit as st
import json
import pandas as pd
import folium
from streamlit_folium import folium_static

# Title for the app
st.title("Visualization of Historical Data")

# Load the JSON data from EN.json
try:
    with open('EN.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
except FileNotFoundError:
    st.error("The file EN.json was not found. Please ensure it is available in the working directory.")
    st.stop()

# Sidebar to select the entry by filename
filenames = [entry['filename'] for entry in data]
selected_file = st.sidebar.selectbox("Select a file to visualize", filenames)

# Find the selected entry in the data
selected_entry = next(item for item in data if item['filename'] == selected_file)

# Extract the site object
site_object = selected_entry['content']['siteObject']

# Display author information
st.header("Author Information")
st.write(f"**Author:** {site_object['author']}")
st.write(f"**Author Publication:** {site_object['authorPublication']}")
st.write(f"**Original Language:** {site_object['originalLanguage']['#text']} ({site_object['originalLanguage']['@xml:lang']})")
st.write(f"**Publication Language:** {site_object['publicationLanguage']['#text']} ({site_object['publicationLanguage']['@xml:lang']})")

# Display date and description
st.header("Description")
st.write(f"**Date:** {site_object['date']}")
st.write(f"**Description:** {site_object['description']}")

# Display geographic coordinates with a map
st.header("Geographic Coordinates")
latitude = site_object['geographicCoordinates'].get('latitude')
longitude = site_object['geographicCoordinates'].get('longitude')

if latitude and longitude:
    st.write(f"**Location:** {site_object['nameSource']} ({site_object['nameContemporary']})")
    latitude, longitude = float(latitude), float(longitude)
    
    # Show the map
    m = folium.Map(location=[latitude, longitude], zoom_start=13)
    folium.Marker([latitude, longitude], tooltip=site_object['nameContemporary']).add_to(m)
    folium_static(m)
else:
    st.write("No geographic coordinates available.")

# Display additional information
st.header("Additional Information")
st.write(f"**Keywords:** {site_object.get('keywords', 'N/A')}")
st.write(f"**Contemporary Age:** {site_object.get('ageContemporary', 'N/A')}")
st.write(f"**Certainty of Localization:** {site_object.get('localizationCertainity', 'N/A')}")

# Display links if available
st.header("External Links")
if site_object.get('geonamesLink'):
    st.write(f"[Geonames Link]({site_object['geonamesLink']})")
if site_object.get('viaf'):
    st.write(f"[VIAF Link]({site_object['viaf']})")

# Display source content
st.header("Source Information")
st.write(f"**Source Information:** {site_object.get('sourceInformation', 'N/A')}")


