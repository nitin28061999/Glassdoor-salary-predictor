import streamlit as st

from predictor import predict_salary

from eda import *

from utils import *

st.set_page_config(
    page_title="Glassdoor Salary Predictor",
    layout="wide"
)

st.title("💼 Glassdoor Salary Prediction")

st.sidebar.title("Navigation")

page = st.sidebar.radio(
    "Go To",
    [
        "Home",
        "EDA",
        "Predict Salary"
    ]
)
if page == "Home":

    st.header("📌 Business Problem")

    st.write("""
This application predicts salaries based on:

- Job Title
- Company Size
- Industry
- Sector
- State
- Company Age
""")

    st.subheader("Dataset")

    st.write("""
The dataset contains Glassdoor job listings collected from different companies.

The machine learning model predicts the expected average salary.
""")

elif page == "EDA":

    st.header("📊 Exploratory Data Analysis")

    st.plotly_chart(salary_distribution(), use_container_width=True)

    st.plotly_chart(top_job_titles(), use_container_width=True)

    st.plotly_chart(company_size_salary(), use_container_width=True)

elif page == "Predict Salary":

    st.header("💰 Salary Prediction")

    job = st.selectbox("Job Title", get_job_titles())

    size = st.selectbox("Company Size", get_sizes())

    industry = st.selectbox("Industry", get_industries())

    sector = st.selectbox("Sector", get_sectors())

    state = st.selectbox("State", get_states())

    age = st.slider("Company Age", 1, 150, 20)

    if st.button("Predict Salary"):

        user_data = {
            "Job Title": job,
            "Size": size,
            "Industry": industry,
            "Sector": sector,
            "State": state,
            "Company Age": age
        }

        prediction = predict_salary(user_data)

        st.success(f"Estimated Salary: ${prediction:.2f}K")
    