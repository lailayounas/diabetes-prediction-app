import streamlit as st
import joblib
import numpy as np

# -----------------------------
# Page Config
# -----------------------------
st.set_page_config(
    page_title="Diabetes Prediction App",
    page_icon="🩺",
    layout="centered"
)

# -----------------------------
# Sidebar
# -----------------------------
st.sidebar.title("Diabetes Predictor")
st.sidebar.info("📌 Enter patient details and click Predict to see the result.")
st.sidebar.image("https://cdn-icons-png.flaticon.com/512/2920/2920347.png", width=120)
# -----------------------------
# Header
# -----------------------------
st.markdown(
    """
    <h1 style='text-align: center; color: #2E86C1;'>
    🩺 Diabetes Risk Predictor
    </h1>
    <p style='text-align: center; font-size:18px; color:#34495E;'>
    Enter patient details below to estimate diabetes risk
    </p>
    """,
    unsafe_allow_html=True
)

# Expander for instructions
with st.expander("ℹ️ How to Use"):
    st.write(
        """
        1. Enter the patient’s health details in the input fields.  
        2. Click the **Predict** button below.  
        3. View the prediction and recommendations.  
        ⚠️ This tool is for educational purposes only.
        """
    )

st.markdown("---")
st.write("Enter patient details below:")

# -----------------------------
# Load model + scaler
# -----------------------------
model = None
scaler = None
try:
    model = joblib.load("diabetes_model.pkl")
    scaler = joblib.load("scaler.pkl")
    st.success("Model & Scaler loaded successfully ✅")
except Exception as e:
    st.error(f"Error loading model/scaler: {e}")

# -----------------------------
# Input Fields (2-column)
# -----------------------------
st.subheader("Patient Details")

col1, col2 = st.columns(2)

with col1:
    pregnancies = st.number_input("Pregnancies", 0, 20, 0)
    glucose = st.number_input("Glucose", 0, 200, 120)
    bp = st.number_input("Blood Pressure", 0, 150, 70)
    skin = st.number_input("Skin Thickness", 0, 100, 20)

with col2:
    insulin = st.number_input("Insulin", 0, 900, 80)
    bmi = st.number_input("BMI", 0.0, 70.0, 25.0)
    dpf = st.number_input("Diabetes Pedigree Function", 0.0, 2.5, 0.5)
    age = st.number_input("Age", 0, 120, 30)

# -----------------------------
# Predict Button
# -----------------------------
if st.button("Predict"):

    if model is None or scaler is None:
        st.error("Model or scaler not loaded ❌")
    else:
        try:
            # Prepare input
            input_data = np.array([[pregnancies, glucose, bp, skin, insulin, bmi, dpf, age]])
            input_data_scaled = scaler.transform(input_data)
            prediction = model.predict(input_data_scaled)

            # Display prediction in colored boxes
            if prediction[0] == 1:
                st.markdown(
                    "<div style='background-color:#F8D7DA; padding:15px; border-radius:10px; text-align:center; color:#721C24; font-weight:bold;'>⚠️ The person is Diabetic</div>",
                    unsafe_allow_html=True
                )
                st.info("👉 Recommendation: Please consult a healthcare professional and monitor glucose levels regularly.")
            else:
                st.markdown(
                    "<div style='background-color:#D4EDDA; padding:15px; border-radius:10px; text-align:center; color:#155724; font-weight:bold;'>✅ The person is Not Diabetic</div>",
                    unsafe_allow_html=True
                )
                st.info("👉 Recommendation: Maintain a healthy lifestyle with balanced diet and exercise.")

            # Medical disclaimer
            st.markdown("---")
            st.warning("⚠️ This tool is for educational purposes only. Do NOT use it as medical advice.")

        except Exception as e:
            st.error(f"Prediction failed: {e}")