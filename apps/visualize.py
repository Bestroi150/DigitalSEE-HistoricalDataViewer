import streamlit as st
import json
import folium
from streamlit_folium import folium_static

def app():
    st.set_page_config(page_title="DigitalSEE", layout="wide")
    
    st.title("🌍 DigitalSEE: Visualize Cultural Data")
    
    # Load JSON data
    try:
        with open('EN.json', 'r', encoding='utf-8') as file:
            data = json.load(file)
    except FileNotFoundError:
        st.error("⚠️ The file `EN.json` was not found. Please ensure it is available in the working directory.")
        st.stop()

    # Sidebar: File selection
    st.sidebar.header("File Selection")
    filenames = [entry['filename'] for entry in data]
    selected_file = st.sidebar.selectbox("Select a file to visualize", filenames)
    
    # Filter the selected entry
    selected_entry = next(item for item in data if item['filename'] == selected_file)
    site_object = selected_entry['content']['siteObject']

    # Author and general information
    st.header("🖋️ Author & Publication Details")
    st.markdown(f"**Author:** `{site_object['author']}`")
    st.markdown(f"**Publication:** `{site_object['authorPublication']}`")
    
    col1, col2 = st.columns(2)
    col1.markdown(f"**Original Language:** `{site_object['originalLanguage']['#text']}` "
                  f"({site_object['originalLanguage']['@xml:lang']})")
    col2.markdown(f"**Publication Language:** `{site_object['publicationLanguage']['#text']}` "
                  f"({site_object['publicationLanguage']['@xml:lang']})")

    # Description and Date
    st.header("📝 Description")
    st.markdown(f"**Date:** `{site_object['date']}`")
    st.markdown(f"**Description:** {site_object['description']}")

    # Display geographic coordinates
    st.header("📍 Geographic Coordinates")
    latitude = site_object['geographicCoordinates'].get('latitude')
    longitude = site_object['geographicCoordinates'].get('longitude')

    if latitude and longitude:
        st.write(f"**Location:** {site_object['nameSource']} (`{site_object['nameContemporary']}`)")
        
        latitude, longitude = float(latitude), float(longitude)
        m = folium.Map(location=[latitude, longitude], zoom_start=13)
        folium.Marker([latitude, longitude], tooltip=site_object['nameContemporary']).add_to(m)
        folium_static(m)
    else:
        st.warning("⚠️ Geographic coordinates not available for this entry.")
    
    # Additional information
    st.header("ℹ️ Additional Information")
    st.markdown(f"**Keywords:** {site_object.get('keywords', 'N/A')}")
    st.markdown(f"**Source Content:** {site_object.get('sourceContent', 'N/A')}")

    st.sidebar.info("🌟 Use the sidebar to select a different file to visualize.")

if __name__ == "__main__":
    app()
