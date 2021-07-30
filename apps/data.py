"""
this will contain the code for displaying all the data and visualizations
"""
import streamlit as st
import numpy as np
import pandas as pd


def app():
    st.title('Data Visualizations')

    # Get the data
    skindf = pd.read_csv('skin_dataframe_with_text.csv')

    # load a table of the data
    st.subheader('Data Information:')
    st.write('The table below displays the possible array of symptoms any skin disorder may present')
    st.dataframe(skindf)

    # Describe the data
    st.write('The possible symptoms:')
    chart = st.bar_chart(skindf.drop('Disease', axis=1))
    st.write('The skin conditions:')
    disease1 = st.bar_chart(skindf.Disease)
