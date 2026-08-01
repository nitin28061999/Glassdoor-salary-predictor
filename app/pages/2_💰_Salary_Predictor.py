import streamlit as st
from app.predictor import predict_salary
from app.utils import get_job_titles, get_sizes, get_industries, get_sectors, get_states

st.title("💰 Salary Prediction")

job = st.selectbox("Job Title", get_job_titles())
size = st.selectbox("Company Size", get_sizes())
industry = st.selectbox("Industry", get_industries())
sector = st.selectbox("Sector", get_sectors())
state = st.selectbox("State", get_states())
company_age = st.slider("Company Age", 1, 150, 20)
rating = st.slider("Company Rating", 0.0, 5.0, 3.5, 0.1)
founded_year = st.number_input("Founded Year", min_value=1800, max_value=2026, value=2005, step=1)
min_salary = st.number_input("Min Salary (K)", min_value=0.0, value=50.0, step=1.0)
max_salary = st.number_input("Max Salary (K)", min_value=0.0, value=150.0, step=1.0)

if st.button("Predict Salary"):

    user = {
        "Job Title": job,
        "Size": size,
        "Industry": industry,
        "Sector": sector,
        "State": state,
        "Company Age": company_age,
        "Rating": rating,
        "Founded": founded_year,
        "Min Salary": min_salary,
        "Max Salary": max_salary,
    }

    prediction = predict_salary(user)

    st.success(f"Estimated Average Salary: **${prediction:.2f}K**")