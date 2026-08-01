import pandas as pd
import google.generativeai as genai
import os

from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY")) # type: ignore

model = genai.GenerativeModel("gemini-2.5-flash") # type: ignore

df = pd.read_csv("../data/processed/glassdoor_jobs_cleaned.csv")


class text:
    def __init__(self, dataframe=df, model_instance=model):
        self.df = dataframe
        self.model = model_instance

    def _dataset_summary(self):
        return (
            f"Dataset Summary\n\n"
            f"Rows: {len(self.df)}\n\n"
            f"Columns:\n\n"
            f"{', '.join(self.df.columns)}\n\n"
            f"Average Salary:\n\n"
            f"{self.df['Average Salary'].describe()}\n"
        )

    def ask(self, question):
        prompt = (
            "You are a Data Science assistant.\n\n"
            "Use this dataset summary to answer.\n\n"
            f"{self._dataset_summary()}\n"
            "Question:\n\n"
            f"{question}"
        )
        response = self.model.generate_content(prompt)
        return response.text


def ask_gemini(question):

    summary = f"""
Dataset Summary

Rows: {len(df)}

Columns:

{', '.join(df.columns)}

Average Salary:

{df['Average Salary'].describe()}
"""

    prompt = f"""
You are a Data Science assistant.

Use this dataset summary to answer.

{summary}

Question:

{question}
"""

    response = model.generate_content(prompt)

    return response.text