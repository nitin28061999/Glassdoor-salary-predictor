import google.generativeai as genai
import os

from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-2.5-flash")


def ask_gemini(question):

    prompt = f"""
You are an AI assistant for a Glassdoor Salary Prediction project.

Answer the user's question clearly and professionally.

Question:
{question}
"""

    response = model.generate_content(prompt)

    return response.text