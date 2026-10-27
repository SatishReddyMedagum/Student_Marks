# STEP 3: STUDENT PASS/FAIL WEB APPLICATION

import pickle
import streamlit as st
import numpy as np

# Set up the web page
st.title("Student Marks Predictor")
st.write("Enter the number of hours studied.")

# Load the saved ML model
with open("Student_marks.pkl", "rb") as file:
    model = pickle.load(file)

# Take input from the user
hours = st.number_input(
    "Study hours",
    min_value=0.0,
    max_value=24.0,
    value=5.0,
    step=0.5
)


if st.button("Predict Marks"):
    input_data = np.array([[hours]])
    prediction = model.predict(input_data)

    marks = float(prediction[0])

    st.success(f"Predicted Marks: {marks:.2f}")

st.caption(
    "Educational demonstration only. "
    "This model is not suitable for real student assessment."
)
