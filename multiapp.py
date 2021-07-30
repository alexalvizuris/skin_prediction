"""
This framework will allow me to incorporate multiple pages in my web app
"""
import streamlit as st



class MultiApp():
    """
    creates multiapp class that will be referenced by application.py
    """
    def __init__(self):
        self.apps = []

    def add_app(self, title, function):
        self.apps.append({
            "title": title,
            "function": function
        })

    def run(self):
        app = st.selectbox('Navigation',
                           self.apps,
                           format_func=lambda app: app['title'])

        app['function']()


