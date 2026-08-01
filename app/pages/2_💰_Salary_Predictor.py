import streamlit as st
from predictor import predict_salary
from utils import *

st.title("💰 Salary Prediction")

job = st.selectbox("Job Title", get_job_titles())
size = st.selectbox("Company Size", get_sizes())
industry = st.selectbox("Industry", get_industries())
sector = st.selectbox("Sector", get_sectors())
state = st.selectbox("State", get_states())
age = st.slider("Company Age", 1, 150, 20)

if st.button("Predict Salary"):

    user = {
        "Job Title": job,
        "Size": size,
        "Industry": industry,
        "Sector": sector,
        "State": state,
        "Company Age": age
    }

    prediction = predict_salary(user)

    st.success(f"Estimated Average Salary: **${prediction:.2f}K**")