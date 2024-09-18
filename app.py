import streamlit as st
from multiapp import MultiApp
from apps import visualize, statistics, map_page

# Create a multi-page app
app = MultiApp()

# Add each application
app.add_app("Visualization", visualize.app)
app.add_app("Statistics", statistics.app)
app.add_app("Map with Descriptions", map_page.app)

# Run the main app
app.run()
