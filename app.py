import streamlit as st
import json
import pandas as pd
import folium
from streamlit_folium import folium_static

# Load the JSON data
data = [
    {
        "filename": "IV_Driesch_PlovdivWalls_1718_EN.xml",
        "content": {
            "siteObject": {
                "author": "Ivan Valchev",
                "nameSource": "Philippopel",
                "nameContemporary": "Пловдив",
                "description": "Герхард Корнелиус фон Дриш наблюдава Пловдив от разстояние поради епидемия в града. Той описва топографията на селището и следите от крепостни стени, които е успял да види.",
                "geographicCoordinates": {
                    "latitude": "42.15151",
                    "longitude": "24.75201"
                },
                "geonamesLink": "https://www.geonames.org/728193/plovdiv.html",
                "date": "08.07.1718",
                "localizationCertainity": "medium",
                "authorPublication": "Gerhard Cornelius von Driesch",
                "ageContemporary": "Late Antiquity",
                "originalLanguage": {
                    "@xml:lang": "lat",
                    "#text": "Latin"
                },
                "publicationLanguage": {
                    "@xml:lang": "deu",
                    "#text": "German"
                },
                "sourceInformation": "Driesch, Gerhard Cornelius von den. Historische Nachricht...",
                "keywords": "Пловдив, Филипопол, топография, крепостни стени",
                "viaf": "https://viaf.org/viaf/194161584/#Driesch,_Gerhard_Cornelius_%CB%9Cvon_den%C5%93_1688-1758"
            }
        }
    }
]

# Extract the site object
site_object = data[0]['content']['siteObject']

# Title for the app
st.title("Visualization of Historical Data")

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
latitude = float(site_object['geographicCoordinates']['latitude'])
longitude = float(site_object['geographicCoordinates']['longitude'])

# Show the map
st.write(f"**Location:** Philippopel (Пловдив)")
m = folium.Map(location=[latitude, longitude], zoom_start=13)
folium.Marker([latitude, longitude], tooltip="Philippopel (Пловдив)").add_to(m)
folium_static(m)

# Display additional information
st.header("Additional Information")
st.write(f"**Keywords:** {site_object['keywords']}")
st.write(f"**Contemporary Age:** {site_object['ageContemporary']}")
st.write(f"**Certainty of Localization:** {site_object['localizationCertainity']}")

# Display links
st.header("External Links")
st.write(f"[Geonames Link]({site_object['geonamesLink']})")
st.write(f"[VIAF Link]({site_object['viaf']})")

# Display source content
st.header("Source Information")
st.write(f"**Source Information:** {site_object['sourceInformation']}")
