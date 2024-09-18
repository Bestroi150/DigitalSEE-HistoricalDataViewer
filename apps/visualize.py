import streamlit as st
import json
import folium
from streamlit_folium import folium_static

def app():
    st.title("DigitalSEE")

    try:
        with open('EN.json', 'r', encoding='utf-8') as file:
            data = json.load(file)
    except FileNotFoundError:
        st.error("The file EN.json was not found. Please ensure it is available in the working directory.")
        st.stop()

    filenames = [entry['filename'] for entry in data]
    selected_file = st.sidebar.selectbox("Select a file to visualize", filenames)
    selected_entry = next(item for item in data if item['filename'] == selected_file)
    site_object = selected_entry['content']['siteObject']

    # Display author and general information
    st.header("Author Information")
    st.write(f"**Author:** {site_object['author']}")
    st.write(f"**Author Publication:** {site_object['authorPublication']}")
    st.write(f"**Original Language:** {site_object['originalLanguage']['#text']} ({site_object['originalLanguage']['@xml:lang']})")
    st.write(f"**Publication Language:** {site_object['publicationLanguage']['#text']} ({site_object['publicationLanguage']['@xml:lang']})")

    # Date and description
    st.header("Description")
    st.write(f"**Date:** {site_object['date']}")
    st.write(f"**Description:** {site_object['description']}")

    # Coordinates and map
    st.header("Geographic Coordinates")
    latitude = site_object['geographicCoordinates'].get('latitude')
    longitude = site_object['geographicCoordinates'].get('longitude')

    if latitude and longitude:
        st.write(f"**Location:** {site_object['nameSource']} ({site_object['nameContemporary']})")
        latitude, longitude = float(latitude), float(longitude)
        m = folium.Map(location=[latitude, longitude], zoom_start=13)
        folium.Marker([latitude, longitude], tooltip=site_object['nameContemporary']).add_to(m)
        folium_static(m)
    else:
        st.write("No geographic coordinates available.")

    st.header("Additional Information")
    st.write(f"**Keywords:** {site_object.get('keywords', 'N/A')}")
    st.write(f"**Source Content:** {site_object.get('sourceContent', 'N/A')}")
