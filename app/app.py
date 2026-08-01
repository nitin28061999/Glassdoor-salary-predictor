import streamlit as st

st.set_page_config(
    page_title="Glassdoor Salary Predictor",
    page_icon="💼",
    layout="wide"
)

st.title("💼 Glassdoor Salary Prediction System")

st.markdown("""
## 📌 Business Problem

The objective of this project is to predict employee salaries based on job attributes such as:

- Job Title
- Company Size
- Industry
- Sector
- Location
- Company Age

---

## 🎯 Project Objectives

- Analyze salary trends
- Compare salaries across job roles
- Study the effect of company size and location
- Build a machine learning model for salary prediction
- Deploy an interactive web application

---

👈 Use the navigation menu on the left to explore the application.
""")
    