# 🏦 Loan Eligibility Prediction App

A machine learning web application that predicts whether a customer is eligible for a loan based on demographic and financial information.

## 🔍 Project Overview
This app uses a pre-trained ML model to classify applicants as "Eligible" or "Not Eligible" for a loan. Built with Python and Streamlit, it's designed for both ease of use and deployment. This personal project simulates a real-world banking use case to demonstrate applied data science skills.

---

## 🚀 Demo
![App Screenshot](screenshot.png) <!-- Optional: Add a screenshot of your app -->

Try the live app: **[Coming Soon]**

---

## 🛠️ Features
- ✅ User-friendly web form to collect input data
- ✅ Predicts loan eligibility in real time
- ✅ CSV upload for batch predictions
- ✅ Displays prediction with confidence score
- ✅ Modular code with clear ML pipeline

---

## 🧠 Machine Learning Model
- **Algorithm**: Logistic Regression (or Random Forest)
- **Libraries**: `scikit-learn`, `pandas`, `numpy`
- **Model Inputs**:
  - Gender
  - Marital Status
  - Education
  - Applicant & Co-applicant Income
  - Loan Amount & Term
  - Credit History
  - Employment Type
  - Property Area

---

## 📁 Project Structure

loan-eligibility-app/
│
├── app.py # Streamlit app
├── model/
│ └── loan_model.pkl # Trained ML model
├── data/
│ └── test_data.csv # Sample input file
├── utils/
│ └── preprocessing.py # Data preprocessing functions
├── requirements.txt # Python dependencies
└── README.md # Project documentation

