"""
this will contain the code for displaying all the data and visualizations
"""
import streamlit as st
import pandas as pd
import plotly.express as px

# this function creates all the graphs
def data_v():
    st.title('Data Information')

    # Get the data
    skindf = pd.read_csv('skin_dataframe_with_text.csv')

    # Display the diseases
    st.write('The skin conditions:')
    disease1 = st.bar_chart(skindf.Disease)

    # Display the symptoms
    st.write('The possible symptoms:')
    chart = st.bar_chart(skindf.drop('Disease', axis=1))

    # Create heatmap that displays most common symptoms per skin condition
    st.write('Most frequent symptoms per skin condition:')
    fig_1 = px.density_contour(skindf, x='Symptom_1', y='Disease')
    st.write(fig_1)
    fig_2 = px.density_contour(skindf, x='Symptom_2', y='Disease')
    st.write(fig_2)

    # Create an area graph that displays the symptoms that are commonly experienced together. Organized by disease.
    st.write('Symptoms commonly experienced together:')
    fig_3 = px.area(skindf, x="Symptom_1", y="Symptom_2", line_group="Disease")
    st.write(fig_3)
