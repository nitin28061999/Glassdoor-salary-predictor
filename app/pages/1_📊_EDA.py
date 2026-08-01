import streamlit as st
from app.eda import salary_distribution, top_job_titles, company_size_salary

st.title("📊 Exploratory Data Analysis")

st.subheader("Salary Distribution")
st.plotly_chart(salary_distribution(), use_container_width=True)

st.subheader("Top Paying Job Titles")
st.plotly_chart(top_job_titles(), use_container_width=True)

st.subheader("Salary by Company Size")
st.plotly_chart(company_size_salary(), use_container_width=True)