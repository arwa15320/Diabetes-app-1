import streamlit as st
import pickle

# Load the model from the pickle file
with open('Model.pkl', 'rb') as file:
    model = pickle.load(file)

# Set the title of the page
st.title("Diabetes Patient Prediction")

# Set up input fields
Age = st.number_input('Age', min_value=0.0, max_value=100.0, value=1.0)
Pregnancies = st.number_input('Pregnancies', min_value=0.0, max_value=10.0, value=1.0)
Glucose = st.number_input('Glucose', min_value=0.0, max_value=200.0, value=1.0)
Insulin = st.number_input('Insulin', min_value=0.0, max_value=846.0, value=1.0)
BMI = st.number_input('BMI', min_value=0.0, max_value=100.0, value=1.0)
DiabetesPedigreeFunction = st.number_input('Diabetes Pedigree Function', min_value=0.0, max_value=2.5, value=1.0)

# Add a button for prediction
if st.button("Predict"):
    # Perform prediction
    output = model.predict([[Pregnancies, Glucose, Insulin, BMI, DiabetesPedigreeFunction, Age]])

    # Display the result
    st.write("Diabetes Prediction: ", "Positive" if output[0] == 1 else "Negative")
else:
    st.write("Enter all features and press 'Predict' to see the result.")
