import pandas as pd
from pathlib import Path

DATA_FILE = Path(__file__).resolve().parent.parent / "Data" / "processed" / "glassdoor_jobs_cleaned.csv"
df = pd.read_csv(DATA_FILE)


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