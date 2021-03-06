"""
this page will display all of the symptoms and provide a prediction model
"""

import pandas as pd
import numpy as np
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from PIL import Image
import streamlit as st

"""
This function takes user input, and encodes that input into numerical format
Those numbers are then returned as a pandas dataframe.
"""
def get_symptoms():
    numeric = []

    # the following variables are the multiselect dropdown controls
    skin = st.sidebar.multiselect(
        'Skin',
        ['nodal skin ruptures', 'discolored patches', 'blackheads', 'puss-filled pimples', 'scarring',
         'peeling',
         'dusting'],
    )

    body = st.sidebar.multiselect(
        'Body & Lifestyle',
        ['joint pain', 'stomach pain', 'spotty urination', 'burning urination', 'loss of appetite', 'malaise',
         'lymph nodes']
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

    # each menu selection is iterated over and added to a list if it is selected
    for i in skin:

        if i == 'nodal skin ruptures':
            numeric.append(3)
        if i == 'discolored patches':
            numeric.append(103)
        if i == 'blackheads':
            numeric.append(124)
        if i == 'puss-filled pimples':
            numeric.append(123)
        if i == 'scarring':
            numeric.append(125)
        if i == 'peeling':
            numeric.append(126)
        if i == 'dusting':
            numeric.append(127)

    for j in body:
        if j == 'joint pain':
            numeric.append(7)
        if j == 'stomach pain':
            numeric.append(8)
        if j == 'spotty urination':
            numeric.append(14)
        if j == 'burning urination':
            numeric.append(13)
        if j == 'loss of appetite':
            numeric.append(36)
        if j == 'malaise':
            numeric.append(49)
        if j == 'lymph nodes':
            numeric.append(48)

    for k in irritation:
        if k == 'itching':
            numeric.append(1)
        if k == 'rash':
            numeric.append(2)
        if k == 'blister':
            numeric.append(130)
        if k == 'red nose sore':
            numeric.append(131)
        if k == 'yellow crust':
            numeric.append(132)
        if k == 'red spots all over':
            numeric.append(100)

    for nail in nails:
        if nail == 'dents in nail':
            numeric.append(128)
        if nail == 'inflamed nail':
            numeric.append(129)

    for m in head:
        if m == 'fatigue':
            numeric.append(15)
        if m == 'lethargy':
            numeric.append(22)
        if m == 'headache':
            numeric.append(32)
        if m == 'mild fever':
            numeric.append(42)
        if m == 'high fever':
            numeric.append(26)

    # if the list is shorter than 17 items, a zero will be added until the list reaches 17 items.
    while len(numeric) < 17:
        numeric.append(0)
    print(numeric)
    symp_np = np.array([numeric])

    # turn data into dataframe
    symptom_df = pd.DataFrame(symp_np, index=[0])
    return symptom_df

"""
This function creates the testing and training data for the SVC model
the get_symptoms() method is called here, and a prediction is made when the user presses the 'submit' button
"""
def condition():
    # Get the data
    df = pd.read_csv('skin_dataframe_with_numbers.csv')

    # Split the data
    data = df.iloc[:, 1:].values
    labels = df['Disease'].values

    # Train and test the data
    x_train, x_test, y_train, y_test = train_test_split(data, labels, shuffle=True, train_size=0.85)

    # Set the subheader
    st.subheader('   ')

    # subheader for sidebar
    st.sidebar.write("""
            # Symptoms 
            """)

    # Store user input into variable
    user_input = get_symptoms()

    # create submit button for symptoms
    result = st.sidebar.button('submit')

    # while the 'submit' button has NOT been selected, the webpage will display an image
    if not result:
        # Title and subtitle
        st.write("""
                # Skin Condition
                Detect which type of skin condition you may have
                """)
        # Open and display image
        image = Image.open('checking-skin.jpg')
        st.image(image, caption='Are you wondering what your skin is telling you?', use_column_width=True)

    # import model
    svc_model = SVC()
    svc_model.fit(x_train, y_train)

    # if button is selected, write prediction of symptoms
    if result:
        st.write("""
                # Our predictive model suggests:
                """)
        preds = svc_model.predict(user_input)

        output_columns = st.columns(2)
        output_columns[0].write('You probably have:')
        output_columns[1].write('Your accuracy:')
        results = st.columns(2)
        results[0].write(str(preds))
        results[1].write(str(accuracy_score(y_test, svc_model.predict(x_test))))

