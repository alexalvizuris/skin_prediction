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

    # adds pages to navigation menu
    def add_app(self, title, function):
        self.apps.append({
            "title": title,
            "function": function
        })

    # removes pages from the navigation menu
    def remove_app(self, title, function):
        self.apps.remove({
            "title": title,
            "function": function
        })

    # calls the function that is listen by the webpage that is selected
    def run(self):
        select = st.selectbox('Navigation',
                              self.apps,
                              format_func=lambda app: app['title'])

        select['function']()
