import pandas as pd

df = pd.read_csv("../data/processed/glassdoor_jobs_cleaned.csv")


def get_job_titles():
    return sorted(df["Job Title"].dropna().unique())


def get_states():
    return sorted(df["State"].dropna().unique())


def get_industries():
    return sorted(df["Industry"].dropna().unique())


def get_sizes():
    return sorted(df["Size"].dropna().unique())


def get_sectors():
    return sorted(df["Sector"].dropna().unique())