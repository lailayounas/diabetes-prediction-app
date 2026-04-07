import streamlit as st
import pickle
import numpy as np

st.title("Diabetes Prediction App")

# Load model safely
try:
    with open("diabetes_model.pkl", "rb") as file:
        model = pickle.load(file)
    st.success("Model loaded ✅")
except Exception as e:
    st.error(f"Model error: {e}")
    #st.stop()   # STOP APP if model fails
    st.write("app started")
# Inputs
pregnancies = st.number_input("Pregnancies", 0, 20, 0)
glucose = st.number_input("Glucose", 0, 200, 120)
bp = st.number_input("Blood Pressure", 0, 150, 70)
skin = st.number_input("Skin Thickness", 0, 100, 20)
insulin = st.number_input("Insulin", 0, 900, 80)
bmi = st.number_input("BMI", 0.0, 70.0, 25.0)
dpf = st.number_input("DPF", 0.0, 2.5, 0.5)
age = st.number_input("Age", 0, 120, 30)

if st.button("Predict"):
    data = np.array([[pregnancies, glucose, bp, skin, insulin, bmi, dpf, age]])
    pred = model.predict(data)
    st.success("Diabetic ✅" if pred[0]==1 else "Not Diabetic ❌")