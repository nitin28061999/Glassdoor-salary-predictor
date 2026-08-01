import pandas as pd
import plotly.express as px

df = pd.read_csv("../data/processed/glassdoor_jobs_cleaned.csv")


def salary_distribution():  # sourcery skip: inline-immediately-returned-variable

    fig = px.histogram(
        df,
        x="Average Salary",
        nbins=25,
        title="Salary Distribution"
    )

    return fig


def top_job_titles():  # sourcery skip: inline-immediately-returned-variable

    top = (
        df.groupby("Job Title")["Average Salary"]
        .mean()
        .sort_values(ascending=False)
        .head(10)
        .reset_index()
    )

    fig = px.bar(
        top,
        x="Average Salary",
        y="Job Title",
        orientation="h",
        title="Top Paying Job Titles"
    )

    return fig


def company_size_salary():  # sourcery skip: inline-immediately-returned-variable

    fig = px.box(
        df,
        x="Size",
        y="Average Salary",
        title="Salary by Company Size"
    )

    return fig