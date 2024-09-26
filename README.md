# DigitalSEE-HistoricalDataViewer

## Overview

**DigitalSEE-HistoricalDataViewer** is an interactive data visualization application built with **Streamlit** and connected to a **[Hugging Face Space](https://huggingface.co/spaces/bestroi/DigitalSEE)**. It provides an easy way to visualize and explore historical geographic data, integrating information like locations, descriptions, and author details on an interactive map. The app utilizes **Folium** for mapping and **Streamlit Folium** for rendering the maps within the Streamlit interface.

The application is structured into two main components: a file selection viewer (`visualization.py`) and an interactive map viewer (`map_page.py`), both designed to interact with a dataset hosted on GitHub.

## Table of Contents

-   [Features](#features)
-   [Usage](#usage)
-   [Installation](#installation)
-   [Components](#components)
    -   [Visualization](#visualizationpy)
    -   [Map Page](#map_pagepy)
-   [Data Source](#data-source)
-   [License](#license)

## Features

-   **File Selection Viewer**: Allows users to select and view historical data files hosted on the project's main GitHub repository - [DigitalSEE](https://github.com/Bestroi150/DigitalSEE).
-   **Interactive Map Viewer**: Displays geographic locations and information using a fully interactive map.
-   **Geographic Data Visualization**: Visualizes latitude and longitude data, with descriptive information and author details.
-   **Multiple Map Layers**: Users can switch between **OpenStreetMap** and **CartoDB** (light and dark mode).
-   **Marker Clustering**: Pins multiple locations on the map using marker clusters for easy navigation.

## Usage

1.  **File Viewer**: Use the sidebar to choose a file to visualize from the list of available datasets.
2.  **Map Viewer**: Explore the map to view locations, descriptions, and other details associated with historical sites. Click on the markers to read more about each site.

The application provides a powerful yet simple and user-friendly interface to explore and interact with historical data using a combination of text details and maps.

## Installation

To run the DigitalSEE-HistoricalDataViewer locally, follow these steps:

1.  **Clone the Repository**:  
    
    `git clone https://github.com/Bestroi150/DigitalSEE-HistoricalDataViewer.git
    cd DigitalSEE-HistoricalDataViewer` 
    
2.  **Install Dependencies**: Make sure you have Python installed, then use `pip` to install required libraries.
    
    `pip install streamlit folium streamlit-folium requests` 
    
3.  **Run the Application**:      
    `streamlit run visualization.py` 
    
    This will start a local server, and you can access the app in your web browser.
    

## Components

### Visualization (`visualization.py`)

-   **Purpose**: This page displays author and publication details of historical sites, alongside geographic data and a description of each entry.
-   **File Selection Sidebar**: Allows users to select a JSON file from the dataset to view its contents.
-   **Map Rendering**: If geographic coordinates are available for a selected entry, the app uses **Folium** to display the location on an interactive map.

### Map Page (`map_page.py`)
-   **Purpose**: Visualizes all the available geographic data on a map, with clusters of markers representing different locations.
-   **Full Screen & Layer Controls**: Users can toggle fullscreen mode and switch between map layers.
-   **Marker Clustering**: Each location in the dataset is represented as a marker, which can be clicked to reveal additional descriptive information.

## Data Source

The data is hosted on GitHub in a JSON master file. The app fetches and parses the dataset from the following URL:

`https://raw.githubusercontent.com/Bestroi150/DigitalSEE/main/JSON/EN.json` 

Each entry in the dataset includes:

-   **Filename**: The identifier for the historical entry.
-   **Author Details**: Information on the author and the publication.
-   **Geographic Coordinates**: Latitude and longitude for mapping.
-   **Description**: A brief summary of the historical site.

## License

Creative Commons Attribution-ShareAlike 4.0 International. See the `LICENSE` file for more details.
