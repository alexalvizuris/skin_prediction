# This program predicts what type of skin condition you may have

import pandas as pd
import numpy as np
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
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

# Split the data
data = df.iloc[:,1:].values
labels = df['Disease'].values

# Train and test the data
x_train, x_test, y_train, y_test = train_test_split(data, labels, shuffle=True, train_size = 0.85)


# Set the subheader
st.subheader('   ')


# subheader for sidebar
st.sidebar.write("""
# Symptoms 
""")

def get_symptoms():

    selected = []
    numeric = []
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

    for i in skin:
        selected.append(i)
        if i == 'nodal skin ruptures':
            numeric.append(4)
        if i == 'discolored patches':
            numeric.append(0)
        if i == 'blackheads':
            numeric.append(2)
        if i == 'puss-filled pimples':
            numeric.append(2)
        if i == 'scurring':
            numeric.append(2)
        if i == 'peeling':
            numeric.append(3)
        if i == 'dusting':
            numeric.append(2)
    for j in body:
        selected.append(j)
        if j == 'joint pain':
            numeric.append(3)
        if j == 'stomach pain':
            numeric.append(5)
        if j == 'spotty urination':
            numeric.append(0)
        if j == 'burning urination':
            numeric.append(6)
        if j == 'loss of appetite':
            numeric.append(4)
        if j == 'malaise':
            numeric.append(6)
        if j == 'lymph nodes':
            numeric.append(6)
    for k in irritation:
        selected.append(k)
        if k == 'itching':
            numeric.append(1)
        if k == 'rash':
            numeric.append(3)
        if k == 'blister':
            numeric.append(4)
        if k == 'red nose sore':
            numeric.append(2)
        if k == 'yellow crust':
            numeric.append(3)
        if k == 'red spots all over':
            numeric.append(3)
    for l in nails:
        selected.append(l)
        if l == 'dents in nail':
            numeric.append(2)
        if l == 'inflamed nail':
            numeric.append(2)
    for m in head:
        selected.append(m)
        if m == 'fatigue':
            numeric.append(4)
        if m == 'lethargy':
            numeric.append(2)
        if m == 'headache':
            numeric.append(3)
        if m == 'mild fever':
            numeric.append(5)
        if m == 'high fever':
            numeric.append(7)

    while len(numeric) < 11:
        numeric.append(0)
    print(numeric)

    symp_np = np.array([numeric])



    # turn data into dataframe
    symptom_df = pd.DataFrame(symp_np, index=[0])
    return symptom_df

# Store user input into variable
user_input = get_symptoms()

# # import model
svc_model = SVC()
svc_model.fit(x_train, y_train)

preds = svc_model.predict(user_input)
print(preds)

st.write('You probably have:', preds)






