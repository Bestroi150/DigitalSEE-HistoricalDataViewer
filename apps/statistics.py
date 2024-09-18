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
                if date_obj.year >= 1677:  # Keep as datetime if within bounds
                    parsed_dates.append(date_obj)
                else:
                    parsed_dates.append(date_str)  # Keep as string if too old
            except ValueError:
                try:
                    # Try parsing only month and year (default day to 1)
                    date_obj = datetime.strptime(date_str, '%m.%Y')  # e.g., "07.1718"
                    if date_obj.year >= 1677:
                        parsed_dates.append(date_obj)
                    else:
                        parsed_dates.append(date_str)
                except ValueError:
                    try:
                        # Try parsing only the year (default month and day to January 1)
                        date_obj = datetime.strptime(date_str, '%Y')  # e.g., "1718"
                        if date_obj.year >= 1677:
                            parsed_dates.append(date_obj)
                        else:
                            parsed_dates.append(date_str)
                    except ValueError:
                        # Skip unrecognized date formats
                        pass

    # Convert dates into a pandas DataFrame
    date_strings = [d if isinstance(d, str) else d.strftime('%Y-%m-%d') for d in parsed_dates]
    date_df = pd.DataFrame(date_strings, columns=['Date'])

    # Sort the dates by treating them as strings for very old dates
    def sort_dates(date_list):
        # Split into two lists: valid datetime objects and string dates
        valid_dates = []
        string_dates = []
        
        for d in date_list:
            try:
                valid_dates.append(datetime.strptime(d, '%Y-%m-%d'))
            except ValueError:
                string_dates.append(d)  # Keep older dates as strings
        
        # Sort the valid dates and string dates separately
        valid_dates_sorted = sorted(valid_dates)
        string_dates_sorted = sorted(string_dates, key=lambda x: (x.split('.')[-1], x))  # Sort strings by year first
        
        # Merge the sorted lists
        return valid_dates_sorted + string_dates_sorted

    sorted_dates = sort_dates(date_strings)
    
    # Display the language counts as a bar chart
    st.header("Original Languages")
    lang_counts = pd.Series(languages).value_counts()
    st.bar_chart(lang_counts)

    # Display the sorted dates
    st.header("Dates of the Files (Sorted by Year, Month, Day)")
    sorted_dates_str = [d.strftime('%Y-%m-%d') if isinstance(d, datetime) else d for d in sorted_dates]
    date_counts = pd.Series(sorted_dates_str).value_counts().sort_index()
    st.line_chart(date_counts)

    # Display raw sorted date data if the user checks the box
    if st.checkbox("Show raw sorted date data"):
        st.subheader("Sorted Date Data")
        st.write(pd.DataFrame(sorted_dates_str, columns=['Date']))
