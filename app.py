"""
This file calls all of the other python files that will be referenced for the multiapp function
"""
import streamlit as st
import prediction
import data
from multiapp import MultiApp
from PIL import Image

hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

multi_app = MultiApp()
admin = 'admin'
verify = True

image = Image.open('touching_face.jpg')

optionals = st.sidebar.beta_expander('Log In', False)
un = optionals.text_input('Username')
pw = optionals.text_input('Password', type='password')
ver = optionals.checkbox('Check this box to proceed')

if un == admin:
    if pw == admin:
        if ver:
            verify = False
            multi_app.add_app('Skin Condition', prediction.condition)
            multi_app.add_app('Data Visualizations', data.data_v)

            multi_app.run()
    elif pw != '':
        st.warning('Please input a valid username or password')
elif un != '':
    st.warning('Please input a valid username or password')

if verify:
    st.title('Log In')
    st.image(image, caption='Are you wondering what your skin is telling you?', use_column_width=True)

