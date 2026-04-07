# Diabetes Prediction App 🩺

[![Python](https://img.shields.io/badge/Python-3.11-blue)](https://www.python.org/)  
[![Streamlit](https://img.shields.io/badge/Streamlit-1.28-green)](https://streamlit.io/)  
[![Hugging Face](https://img.shields.io/badge/Hosted%20on-Hugging%20Face-orange)](https://huggingface.co/spaces/laila123younas/diabetes-prediction-app)  
[![License](https://img.shields.io/badge/License-MIT-yellow)](LICENSE)

---

## Overview
The **Diabetes Prediction App** predicts the likelihood of diabetes in a person based on health parameters.  
It uses a **machine learning model** trained on real datasets and provides instant predictions via a **user-friendly Streamlit interface**.  

**Key Benefits:**  
- Quick diabetes risk assessment  
- Clean and simple interface  
- Deployable locally or on Hugging Face Spaces  

---

## Live Demo
You can access the app here: [Hugging Face](https://huggingface.co/spaces/laila123younas/diabetes-prediction-app)

---

## App Preview
<!-- PLACEHOLDER FOR SCREENSHOT OR GIF -->
<!-- Step 1: Record a short GIF showing the app in action (entering values + Predict button). -->
<!-- Step 2: Save the GIF in the `assets/` folder, e.g., assets/demo.gif -->
<!-- Step 3: Replace the path below with your GIF path -->

![App Demo](assets/demo.gif)  <!-- <-- Replace 'assets/demo.gif' with your actual GIF file -->

---

## Features
- Predict diabetes risk based on user input  
- Preprocessing using `scaler.pkl` for accurate predictions  
- Lightweight and easy to deploy locally or on the cloud  
- Optional Docker support  

---

## Installation (Local Deployment)

### 1. Clone the repository
```bash
git clone <your-repo-link>
cd <your-repo-folder>
2. Create a virtual environment
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
3. Install dependencies
pip install -r requirements.txt
4. Run the app
streamlit run app.py
Hugging Face Deployment
Create a new Space on Hugging Face
 using Streamlit.
Upload your project files:
app.py
diabetes_model.pkl
scaler.pkl
requirements.txt
Optional: assets/ folder for screenshots or GIFs
Hugging Face automatically installs dependencies and hosts the app.
Your app is live at: https://huggingface.co/spaces/laila123younas/diabetes-prediction-app
Docker Deployment
# Build Docker image
docker build -t diabetes-prediction-app .

# Run container
docker run -p 8501:8501 diabetes-prediction-app
Project Structure
diabetes-prediction-app/
│
├── app.py                 # Streamlit app
├── diabetes_model.pkl     # Trained ML model
├── scaler.pkl             # Preprocessing scaler
├── requirements.txt       # Dependencies
├── Dockerfile             # Optional Docker setup
├── README.md              # Documentation
├── .gitignore             # Git ignore rules
└── assets/                # <-- Put screenshots or GIFs here
    └── demo.gif           # <-- Example GIF file
Technologies Used
Python – Programming language
Streamlit – Web interface
scikit-learn – Machine learning
NumPy & Pandas – Data processing
Docker – Optional deployment
Hugging Face Spaces – Cloud deployment
Contributing

Contributions are welcome!

Fork the repository
Create a new branch (git checkout -b feature-name)
Commit your changes (git commit -m "Add feature")
Push to the branch (git push origin feature-name)
Open a Pull Request
<!-- END OF README -->
