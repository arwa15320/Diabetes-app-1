import streamlit as st
import pandas as pd
import numpy as np



# Streamlit app title
st.title("Diabetes Prediction")

# Collecting user input for the model
st.header("Input Features")

pregnancies = st.number_input("Pregnancies", min_value=0, max_value=20, value=0)
glucose = st.number_input("Glucose", min_value=0, max_value=200, value=120)
blood_pressure = st.number_input("Blood Pressure", min_value=0, max_value=140, value=70)
skin_thickness = st.number_input("Skin Thickness", min_value=0, max_value=99, value=20)
insulin = st.number_input("Insulin", min_value=0, max_value=846, value=79)
bmi = st.number_input("BMI", min_value=0.0, max_value=67.0, value=25.0)
dpf = st.number_input("Diabetes Pedigree Function", min_value=0.0, max_value=2.5, value=0.5)
age = st.number_input("Age", min_value=0, max_value=120, value=33)

# Create a button for prediction
if st.button("Predict"):
    # Create a DataFrame from user input
    input_data = pd.DataFrame({
        'Pregnancies': [pregnancies],
        'Glucose': [glucose],
        'BloodPressure': [blood_pressure],
        'SkinThickness': [skin_thickness],
        'Insulin': [insulin],
        'BMI': [bmi],
        'DiabetesPedigreeFunction': [dpf],
        'Age': [age]
    })

    # Convert DataFrame to NumPy array (if necessary)
    input_data_array = input_data.values

    # Predict the outcome
    try:
        prediction = diabetes_model (1).predict(input_data_array)
        
        # Display the result
        if prediction[0] == 1:
            st.write("The model predicts that the person **has diabetes**.")
        else:
            st.write("The model predicts that the person **does not have diabetes**.")
    
    except Exception as e:
        st.write(f"An error occurred: {e}")
