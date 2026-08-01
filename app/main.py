import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

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
    