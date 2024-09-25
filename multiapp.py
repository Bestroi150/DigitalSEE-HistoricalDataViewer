import streamlit as st

class MultiApp:
    def __init__(self):
        self.apps = []

    def add_app(self, title, func):
        self.apps.append({
            "title": title,
            "function": func
        })

    def run(self):
        # Initialize session state if not already initialized
        if 'selected_app' not in st.session_state:
            st.session_state.selected_app = self.apps[0]['title']

        # Sidebar app selection
        selected_title = st.sidebar.selectbox(
            'Navigation',
            [app['title'] for app in self.apps],
            index=[app['title'] for app in self.apps].index(st.session_state.selected_app)
        )

        # Update session state with selected app
        st.session_state.selected_app = selected_title

        # Run the selected app's function
        for app in self.apps:
            if app['title'] == selected_title:
                app['function']()
                break
