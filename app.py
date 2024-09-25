import streamlit as st
from multiapp import MultiApp
from apps import visualize, map_page

# Create a multi-page app
app = MultiApp()


# Add each application
app.add_app("Visualization", visualize.app)
app.add_app("Map", map_page.app)



# Run the main app
app.run()
