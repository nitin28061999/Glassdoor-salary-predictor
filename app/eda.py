import streamlit as st
from app.eda import (
    salary_distribution,
    salary_boxplot_overall,
    top_job_titles,
    job_count_by_title,
    min_max_salary_range,
    rating_distribution,
    company_size_salary,
    ownership_distribution,
    revenue_vs_salary,
    salary_by_sector,
    salary_by_industry,
    salary_by_state,
    job_count_by_state,
    correlation_heatmap,
    age_vs_salary,
    rating_vs_salary,
)

st.title("📊 Exploratory Data Analysis")

tab1, tab2, tab3, tab4 = st.tabs(
    ["Salary Overview", "Company Factors", "Industry & Location", "Relationships"]
)

with tab1:
    st.subheader("Salary Distribution")
    st.plotly_chart(salary_distribution(), use_container_width=True) # pyright: ignore[reportCallIssue]

    st.subheader("Overall Salary Spread & Outliers")
    st.plotly_chart(salary_boxplot_overall(), use_container_width=True) # pyright: ignore[reportCallIssue]

    st.subheader("Top Paying Job Titles")
    st.plotly_chart(top_job_titles(), use_container_width=True) # pyright: ignore[reportCallIssue]

    st.subheader("Most Frequently Posted Job Titles")
    st.plotly_chart(job_count_by_title(), use_container_width=True) # pyright: ignore[reportCallIssue]

    st.subheader("Typical Salary Range by Role")
    st.plotly_chart(min_max_salary_range(), use_container_width=True) # pyright: ignore[reportCallIssue]

with tab2:
    st.subheader("Company Rating Distribution")
    st.plotly_chart(rating_distribution(), use_container_width=True) # pyright: ignore[reportCallIssue]

    st.subheader("Salary by Company Size")
    st.plotly_chart(company_size_salary(), use_container_width=True) # pyright: ignore[reportCallIssue]

    st.subheader("Job Postings by Ownership Type")
    st.plotly_chart(ownership_distribution(), use_container_width=True) # pyright: ignore[reportCallIssue]

    st.subheader("Salary by Revenue Bracket")
    st.plotly_chart(revenue_vs_salary(), use_container_width=True) # pyright: ignore[reportCallIssue]

with tab3:
    st.subheader("Salary by Sector")
    st.plotly_chart(salary_by_sector(), use_container_width=True) # pyright: ignore[reportCallIssue]

    st.subheader("Salary by Industry")
    st.plotly_chart(salary_by_industry(), use_container_width=True) # pyright: ignore[reportCallIssue]

    st.subheader("Top 10 States by Average Salary")
    st.plotly_chart(salary_by_state(), use_container_width=True) # pyright: ignore[reportCallIssue]

    st.subheader("Top 10 States by Job Posting Volume")
    st.plotly_chart(job_count_by_state(), use_container_width=True) # pyright: ignore[reportCallIssue]

with tab4:
    st.subheader("Feature Correlation Heatmap")
    st.plotly_chart(correlation_heatmap(), use_container_width=True) # pyright: ignore[reportCallIssue]

    st.subheader("Average Salary by Company Age")
    st.plotly_chart(age_vs_salary(), use_container_width=True) # pyright: ignore[reportCallIssue]

    st.subheader("Company Rating vs Average Salary")
    st.plotly_chart(rating_vs_salary(), use_container_width=True) # pyright: ignore[reportCallIssue]