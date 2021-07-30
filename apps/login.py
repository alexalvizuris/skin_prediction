"""
login page for web application
"""
import streamlit as st
from apps import prediction, data
import application


def app():

    st.title('Login')

    un = st.text_input('Username')
    pw = st.text_input('Password', type='password')
    ver = st.checkbox('Check this box to proceed')
    admin = 'admin'

    if ver:
        if un == admin:
            if pw == admin:
                application.application.add_app('Skin Condition', prediction.app)
                application.application.add_app('Data Visualizations', data.app)
