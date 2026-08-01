import os
import pandas as pd
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-2.5-flash")

# Load dataset
df = pd.read_csv("../data/processed/glassdoor_jobs_cleaned.csv")


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