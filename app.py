# This program predicts what type of skin condition you may have

import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
# from sklearn.ensemble import SVC
from PIL import Image
import streamlit as st

# Title and subtitle
st.write("""
# Skin Condition
Detect which type of skin condition you may have
""")

# Open and display image
image = Image.open('checking-skin.jpg')
st.image(image, caption='Are you wondering what your skin is telling you?', use_column_width=True)

# Get the data
df = pd.read_csv('dataset.csv')

# Set the subheader
st.subheader('Data Info')

# Show data as table
st.dataframe(df)

# # Show statistics on the data
# st.write(df.describe())
#
# # Show the data as chart
# chart = st.bar_chart(df)

options = st.multiselect(
    'What are your favorite colors',
     ['Green', 'Yellow', 'Red', 'Blue'],
     ['Yellow', 'Red'])

st.write('You selected:', options)

