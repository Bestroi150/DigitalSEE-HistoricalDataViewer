import streamlit as st
import pandas as pd
import json
import matplotlib.pyplot as plt

def app():
    st.title("Statistics of Historical Data")

    try:
        with open('EN.json', 'r', encoding='utf-8') as file:
            data = json.load(file)
    except FileNotFoundError:
        st.error("The file EN.json was not found. Please ensure it is available in the working directory.")
        st.stop()

    # Collecting the original languages and dates
    languages = [entry['content']['siteObject']['originalLanguage']['#text'] for entry in data]
    dates = [entry['content']['siteObject']['date'] for entry in data if entry['content']['siteObject']['date']]

    # Create DataFrames for visualization
    lang_df = pd.DataFrame(languages, columns=['Original Language'])
    date_df = pd.DataFrame(dates, columns=['Date'])

    st.header("Original Languages")
    lang_counts = lang_df['Original Language'].value_counts()
    st.bar_chart(lang_counts)

    st.header("Dates of the Files")
    st.line_chart(date_df['Date'].value_counts().sort_index())

    # Display raw data if the user wants
    if st.checkbox("Show raw data for languages and dates"):
        st.subheader("Raw Data")
        st.write(lang_df)
        st.write(date_df)
