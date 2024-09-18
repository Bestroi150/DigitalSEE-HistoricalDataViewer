import streamlit as st
import pandas as pd
import json
from datetime import datetime

def app():
    st.title("Statistics of Historical Data")

    # Load the JSON data from EN.json
    try:
        with open('EN.json', 'r', encoding='utf-8') as file:
            data = json.load(file)
    except FileNotFoundError:
        st.error("The file EN.json was not found. Please ensure it is available in the working directory.")
        st.stop()

    # Collect original languages
    languages = [entry['content']['siteObject']['originalLanguage']['#text'] for entry in data]

    # Process dates and handle different formats
    parsed_dates = []
    for entry in data:
        date_str = entry['content']['siteObject']['date']
        if date_str:
            date_obj = None
            try:
                # Try parsing the full date (day, month, year)
                date_obj = datetime.strptime(date_str, '%d.%m.%Y')  # e.g., "08.07.1718"
            except ValueError:
                try:
                    # Try parsing only month and year (default day to 1)
                    date_obj = datetime.strptime(date_str, '%m.%Y')  # e.g., "07.1718"
                except ValueError:
                    try:
                        # Try parsing only the year (default month and day to January 1)
                        date_obj = datetime.strptime(date_str, '%Y')  # e.g., "1718"
                    except ValueError:
                        # Skip unrecognized date formats
                        pass

            if date_obj:
                parsed_dates.append(date_obj)

    # Convert the list of dates to a pandas DataFrame
    if parsed_dates:
        date_df = pd.DataFrame(parsed_dates, columns=['Date'])

        # Ensure the Date column is a datetime object (this is a safety check)
        date_df['Date'] = pd.to_datetime(date_df['Date'])

        # Create Year, Month, and Day columns to facilitate sorting
        date_df['Year'] = date_df['Date'].dt.year
        date_df['Month'] = date_df['Date'].dt.month.fillna(1).astype(int)  # Fill missing months with 1 (January)
        date_df['Day'] = date_df['Date'].dt.day.fillna(1).astype(int)  # Fill missing days with 1

        # Sort the DataFrame by Year, Month, and Day
        date_df = date_df.sort_values(by=['Year', 'Month', 'Day'], ascending=True).reset_index(drop=True)

        # Display the language counts as a bar chart
        st.header("Original Languages")
        lang_counts = pd.Series(languages).value_counts()
        st.bar_chart(lang_counts)

        # Display the sorted dates as a line chart
        st.header("Dates of the Files (Sorted by Year, Month, Day)")
        st.line_chart(date_df['Date'].dt.strftime('%Y-%m-%d').value_counts().sort_index())

        # Display raw sorted date data if the user checks the box
        if st.checkbox("Show raw sorted date data"):
            st.subheader("Sorted Date Data")
            st.write(date_df[['Date']])
    else:
        st.write("No valid dates found in the dataset.")
