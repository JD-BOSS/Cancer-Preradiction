import streamlit as st
import numpy as np
import pandas as pd
from sklearn.tree import DecisionTreeClassifier

data = pd.read_csv("E:\MLP\Diabetes\Model\diabetes dataset.csv")  
x = data.iloc[:,:-1]
y = data.iloc[:, -1]
# Train the model
model=DecisionTreeClassifier()
model.fit(x, y)
# Function to predict EMISSION using the loaded model
def predict(Gender,Age,Smoking,Fatigue,Allergy):
    features = np.asarray([Gender,Age,Smoking,Fatigue,Allergy])
    features = features.reshape(1,-1)
    emission = model.predict(features)
    if emission==1:
        return "Affected by Cancer"
    else:
        return "You are safe"

# Streamlit UI
st.title('Cancer PREDICTION')
st.write("Returns Yours:")

#Gender	Age	Smoking	Fatigue	Allergy


# Input fields for user
Gender = st.number_input('Gender')
Age = st.number_input('Age')
Smoking = st.number_input('Smoking')
Fatigue = st.number_input('Fatigue')
Allergy = st.number_input('Allergy')


# Prediction button
if st.button('Predict'):
    # Predict EMISSION
    prediction = predict(Gender,Age,Smoking,Fatigue,Allergy)
    st.write(f"PREDICTION: {prediction}")