import streamlit as st
import pandas as pd
import json
from datetime import datetime

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

    # Process dates and handle different formats
    dates = []
    for entry in data:
        date_str = entry['content']['siteObject']['date']
        if date_str:
            try:
                # Try to parse full date (year, month, day)
                date_obj = datetime.strptime(date_str, '%d.%m.%Y')  # Example: 08.07.1718
            except ValueError:
                try:
                    # Try to parse year and month (default day to 1)
                    date_obj = datetime.strptime(date_str, '%m.%Y')  # Example: 07.1718
                except ValueError:
                    try:
                        # Parse only the year (default month to January and day to 1)
                        date_obj = datetime.strptime(date_str, '%Y')  # Example: 1718
                    except ValueError:
                        date_obj = None  # Invalid or unexpected format, skip this date

            if date_obj:
                dates.append(date_obj)

    # Convert to DataFrame for easier handling and sorting
    date_df = pd.DataFrame(dates, columns=['Date'])
    date_df['Year'] = date_df['Date'].dt.year
    date_df['Month'] = date_df['Date'].dt.month
    date_df['Day'] = date_df['Date'].dt.day

    # Sort the DataFrame by Year, Month, and Day
    date_df = date_df.sort_values(by=['Year', 'Month', 'Day'], ascending=True).reset_index(drop=True)

    st.header("Original Languages")
    lang_counts = pd.Series(languages).value_counts()
    st.bar_chart(lang_counts)

    st.header("Dates of the Files (Sorted by Year, Month, Day)")
    st.line_chart(date_df['Date'].dt.strftime('%Y-%m-%d').value_counts().sort_index())

    # Display raw sorted data if the user wants
    if st.checkbox("Show raw sorted date data"):
        st.subheader("Sorted Date Data")
        st.write(date_df[['Date']])

