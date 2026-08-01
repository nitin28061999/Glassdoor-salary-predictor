import os
import pandas as pd
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

genai = None
model = None
if GEMINI_API_KEY:
    try:
        import google.generativeai as genai

        genai.configure(api_key=GEMINI_API_KEY)
        model = genai.GenerativeModel("gemini-2.5-flash")
    except Exception:
        genai = None

DATA_FILE = Path(__file__).resolve().parent.parent / "Data" / "processed" / "glassdoor_jobs_cleaned.csv"
df = pd.read_csv(DATA_FILE)


def ask_gemini(question):
    if model is None:
        raise RuntimeError(
            "Gemini is not configured. Please set GEMINI_API_KEY in a .env file or the environment."
        )

    dataset_summary = f"""
Dataset Information

Number of records: {len(df)}

Columns:
{', '.join(df.columns)}

Salary Statistics:
{df['Average Salary'].describe().to_string()}
"""

    prompt = f"""
You are an AI assistant helping users understand a Glassdoor Salary Prediction project.

Use the following dataset summary when answering.

{dataset_summary}

Question:
{question}

Provide a clear and professional answer.
"""

    response = model.generate_content(prompt)
    return response.text


def ask_gemini(question):

    dataset_summary = f"""
Dataset Information

Number of records: {len(df)}

Columns:
{', '.join(df.columns)}

Salary Statistics:
{df['Average Salary'].describe().to_string()}
"""

    prompt = f"""
You are an AI assistant helping users understand a Glassdoor Salary Prediction project.

Use the following dataset summary when answering.

{dataset_summary}

Question:
{question}

Provide a clear and professional answer.
"""

    response = model.generate_content(prompt)

    return response.text