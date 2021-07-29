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
df = pd.read_csv('skin_data1.csv')

# Set the subheader
st.subheader('   ')


# subheader for sidebar
st.sidebar.write("""
# Symptoms 
""")

def get_symptoms():

    selected = []
    skin = st.sidebar.multiselect(
        'Skin',
         ['nodal skin ruptures', 'discolored patches', 'blackheads', 'puss-filled pimples', 'scurring', 'peeling', 'dusting'],
         )

    body = st.sidebar.multiselect(
        'Body & Lifestyle',
        ['joint pain', 'stomach pain', 'spotty urination', 'burning urination', 'loss of appetite', 'malaise', 'lymph nodes']
    )

    irritation = st.sidebar.multiselect(
        'Irritation',
        ['itching', 'rash', 'blister', 'red nose sore', 'yellow crust', 'red spots all over']
    )

    nails = st.sidebar.multiselect(
        'Nails',
        ['dents in nail', 'inflamed nail']
    )

    head = st.sidebar.multiselect(
        'Head & Cognitive',
        ['fatigue', 'lethargy', 'headache', 'mild fever', 'high fever']
    )

    # store a dictionary of the symptoms into a variable
    # symp_dict = {
    #     'skin': skin,
    #     'body': body,
    #     'irritation': irritation,
    #     'nails': nails,
    #     'head': head
    # }

    selected.append(skin)
    selected.append(body)
    selected.append(irritation)
    selected.append(nails)
    selected.append(head)


    # turn data into dataframe
    symptom_df = pd.DataFrame(selected, index=[0])
    return symptom_df

# Store user input into variable
user_input = get_symptoms()




