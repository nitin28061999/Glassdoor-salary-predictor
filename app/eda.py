import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from pathlib import Path

DATA_FILE = Path(__file__).resolve().parent.parent / "Data" / "processed" / "glassdoor_jobs_cleaned.csv"
df = pd.read_csv(DATA_FILE)

REVENUE_ORDER = [
    "Less than $1 million (USD)",
    "$1 to $5 million (USD)",
    "$5 to $10 million (USD)",
    "$10 to $25 million (USD)",
    "$25 to $50 million (USD)",
    "$50 to $100 million (USD)",
    "$100 to $500 million (USD)",
    "$500 million to $1 billion (USD)",
    "$1 to $2 billion (USD)",
    "$2 to $5 billion (USD)",
    "$5 to $10 billion (USD)",
    "$10+ billion (USD)",
]


def _valid_age_df():
    return df[(df["Company Age"] > 0) & (df["Company Age"] < 300)]


def salary_distribution():
    fig = px.histogram(df, x="Average Salary", nbins=25, title="Salary Distribution", marginal="box")
    return fig


def salary_boxplot_overall():
    fig = px.box(df, y="Average Salary", points="outliers", title="Overall Salary Spread & Outliers")
    return fig


def top_job_titles():
    top = (df.groupby("Job Title")["Average Salary"].mean().sort_values(ascending=False).head(10).reset_index())
    fig = px.bar(top, x="Average Salary", y="Job Title", orientation="h", title="Top Paying Job Titles")
    fig.update_yaxes(categoryorder="total ascending")
    return fig


def job_count_by_title():
    counts = df["Job Title"].value_counts().head(15).reset_index()
    counts.columns = ["Job Title", "Postings"]
    fig = px.bar(counts, x="Postings", y="Job Title", orientation="h", title="Most Frequently Posted Job Titles")
    fig.update_yaxes(categoryorder="total ascending")
    return fig


def min_max_salary_range():
    top_titles = df["Job Title"].value_counts().head(10).index
    sub = (df[df["Job Title"].isin(top_titles)].groupby("Job Title")[["Min Salary", "Max Salary"]].mean().sort_values("Max Salary").reset_index())

    fig = go.Figure()
    for _, row in sub.iterrows():
        fig.add_trace(go.Scatter(
            x=[row["Min Salary"], row["Max Salary"]],
            y=[row["Job Title"], row["Job Title"]],
            mode="lines", line=dict(color="lightgray", width=4),
            showlegend=False, hoverinfo="skip",
        ))
    fig.add_trace(go.Scatter(x=sub["Min Salary"], y=sub["Job Title"], mode="markers", name="Avg Min Salary", marker=dict(color="#2E6F6E", size=10)))
    fig.add_trace(go.Scatter(x=sub["Max Salary"], y=sub["Job Title"], mode="markers", name="Avg Max Salary", marker=dict(color="#C9A227", size=10)))
    fig.update_layout(title="Typical Salary Range by Role (Top 10 Most Common Titles)")
    return fig


def rating_distribution():
    fig = px.histogram(df, x="Rating", nbins=20, title="Company Rating Distribution")
    return fig


def company_size_salary():
    fig = px.violin(df, x="Size", y="Average Salary", box=True, points=False, title="Salary by Company Size")
    return fig


def ownership_distribution():
    counts = df["Type of ownership"].value_counts().reset_index()
    counts.columns = ["Type of ownership", "Count"]
    fig = px.pie(counts, names="Type of ownership", values="Count", title="Job Postings by Ownership Type", hole=0.4)
    return fig


def revenue_vs_salary():
    sub = df[df["Revenue"].isin(REVENUE_ORDER)]
    fig = px.box(sub, x="Revenue", y="Average Salary", category_orders={"Revenue": REVENUE_ORDER}, title="Salary by Company Revenue Bracket")
    fig.update_xaxes(tickangle=-35)
    return fig


def salary_by_sector():
    top_sectors = df["Sector"].value_counts().head(8).index
    sub = df[df["Sector"].isin(top_sectors)]
    fig = px.box(sub, x="Sector", y="Average Salary", title="Salary by Sector (Top 8 by Job Count)")
    fig.update_xaxes(tickangle=-30)
    return fig


def salary_by_industry():
    top_industries = df["Industry"].value_counts().head(10).index
    sub = df[df["Industry"].isin(top_industries)]
    fig = px.box(sub, x="Industry", y="Average Salary", title="Salary by Industry (Top 10 by Job Count)")
    fig.update_xaxes(tickangle=-35)
    return fig


def salary_by_state():
    top = (df.groupby("State")["Average Salary"].mean().sort_values(ascending=False).head(10).reset_index())
    fig = px.bar(top, x="State", y="Average Salary", title="Top 10 States by Average Salary")
    return fig


def job_count_by_state():
    counts = df["State"].value_counts().head(10).reset_index()
    counts.columns = ["State", "Postings"]
    fig = px.bar(counts, x="State", y="Postings", title="Top 10 States by Job Posting Volume")
    return fig


def correlation_heatmap():
    numeric_cols = ["Rating", "Min Salary", "Max Salary", "Average Salary", "Company Age"]
    sub = _valid_age_df()[numeric_cols]
    corr = sub.corr()
    fig = px.imshow(corr, text_auto=".2f", title="Correlation Between Numeric Features", color_continuous_scale="RdBu_r", zmin=-1, zmax=1)
    return fig


def age_vs_salary():
    sub = _valid_age_df().copy()
    bins = [0, 5, 10, 20, 50, 100, 300]
    labels = ["0-5", "6-10", "11-20", "21-50", "51-100", "100+"]
    sub["Age Bracket"] = pd.cut(sub["Company Age"], bins=bins, labels=labels)
    grouped = sub.groupby("Age Bracket", observed=True)["Average Salary"].mean().reset_index()
    fig = px.bar(grouped, x="Age Bracket", y="Average Salary", title="Average Salary by Company Age")
    return fig


def rating_vs_salary():
    fig = px.scatter(df, x="Rating", y="Average Salary", opacity=0.5, marginal_y="histogram", title="Company Rating vs Average Salary")
    return fig
