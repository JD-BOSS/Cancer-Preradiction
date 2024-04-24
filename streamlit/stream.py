import streamlit as st
import pickle
import numpy as np
import os

# Load the saved Linear Regression model
with open('Cancer.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

# Function to predict GDP per capita using the loaded model
def predict_Cancer(Gender,Age,Smoking,Fatigue,Allergy):
    features = np.array([Gender,Age,Smoking,Fatigue,Allergy])
    features = features.reshape(1,-1)
    Cancer = model.predict(features)
    return Cancer[0]

# Streamlit UI

st.title('Cancer prediction')
st.write("""  
Enter the values for the input features to predict the Cancer.
""")

# Input fields for user
Gender = st.number_input('Gender')
Age = st.number_input('Age')
Smoking = st.number_input('Smoking')
Fatigue = st.number_input('Fatigue')                                          
Allergy= st.number_input('Allergy')


# Prediction button
if st.button('Predict'):
    # Predict Sport
    Cancer_prediction = predict_Cancer(Gender,Age,Smoking,Fatigue,Allergy)
    st.write(f"Predicted Value: {Cancer_prediction}")

    