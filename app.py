import streamlit as st

st.set_page_config(
    page_title="Glassdoor Salary Predictor",
    page_icon="💼",
    layout="wide"
)

st.title("💼 Glassdoor Salary Prediction System")

st.markdown("""
## Welcome!

This project predicts salaries using Machine Learning and analyzes Glassdoor job data.

### Features

- 📊 Exploratory Data Analysis
- 💰 Salary Prediction
- 📈 Model Performance
- 🤖 Gemini AI Assistant

Use the navigation menu on the left to explore the project.
""")

st.info("Select a page from the sidebar.")