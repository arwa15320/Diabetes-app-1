import streamlit as st
import pickle
import pandas as pd



st.title("Diabetes Prediction")


# Input features
st.subheader("Please enter the features below:")

# Collecting input features based on the typical diabetes dataset
pregnancies = st.number_input("Pregnancies", min_value=0, max_value=20, value=0)
glucose = st.number_input("Glucose", min_value=0, max_value=200, value=120)
blood_pressure = st.number_input("Blood Pressure", min_value=0, max_value=140, value=70)
skin_thickness = st.number_input("Skin Thickness", min_value=0, max_value=99, value=20)
insulin = st.number_input("Insulin", min_value=0, max_value=846, value=79)
bmi = st.number_input("BMI", min_value=0.0, max_value=67.0, value=25.0)
dpf = st.number_input("Diabetes Pedigree Function", min_value=0.0, max_value=2.5, value=0.5)
age = st.number_input("Age", min_value=0, max_value=120, value=33)

# Button to trigger the prediction
if st.button("Predict"):
    try:
        # Load the model
        with open('Model.pkl', 'rb') as file:
            model = pickle.load(file)
        
        # Create a DataFrame for the input features
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

        # Perform prediction
        result = model.predict(input_data)

        # Display the result
        st.write("The predicted value is:")
        st.write("**Has Diabetes**" if result[0] == 1 else "**Does Not Have Diabetes**")

    except Exception as e:
        st.error(f"An error occurred: {e}")
else:
    st.write("Please input all features and press 'Predict' to see the result.")
