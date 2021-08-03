"""
This framework will allow me to incorporate multiple pages in my web app
"""
import streamlit as st


class MultiApp():
    """
    creates multiapp class that will be referenced by app.py
    """

    def __init__(self):
        self.apps = []

    def add_app(self, title, function):
        self.apps.append({
            "title": title,
            "function": function
        })

    def remove_app(self, title, function):
        self.apps.remove({
            "title": title,
            "function": function
        })

    def run(self):
        select = st.selectbox('Navigation',
                              self.apps,
                              format_func=lambda app: app['title'])

        select['function']()
