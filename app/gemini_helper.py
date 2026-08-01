import os
from dotenv import load_dotenv
import google.generativeai as genai
from google.generativeai.generative_models import GenerativeModel

# Load environment variables
load_dotenv()

# Configure Gemini
api_key = os.getenv("GEMINI_API_KEY")
if api_key:
    os.environ["GEMINI_API_KEY"] = api_key

# Initialize Gemini
genai.configure(api_key=api_key) # pyright: ignore[reportPrivateImportUsage]

# Initialize Gemini model name
MODEL_NAME = "gemini-2.5-flash"


def ask_gemini(question):
    prompt = f"""
You are an AI assistant for a Glassdoor Salary Prediction project.

Answer the following question in a clear, professional, and concise manner.

Question:
{question}
"""

    model = genai.GenerativeModel(model_name=MODEL_NAME) # pyright: ignore[reportPrivateImportUsage]
    response = model.generate_content(prompt)
    return response.text