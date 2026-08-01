import os
import pandas as pd
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

model = None
genai_module = None
GENAI_INIT_ERROR = None

if GEMINI_API_KEY:
    try:
        import google.generativeai as genai

        genai.configure(api_key=GEMINI_API_KEY)
        model = genai.GenerativeModel("gemini-2.5-flash")
        genai_module = genai
    except Exception as e:
        GENAI_INIT_ERROR = e
        try:
            import google.genai as genai # pyright: ignore[reportMissingImports]

            genai.configure(api_key=GEMINI_API_KEY)
            model = genai.GenerativeModel()
            genai_module = genai
        except Exception as e2:
            GENAI_INIT_ERROR = e2
            model = None

DATA_FILE = Path(__file__).resolve().parent.parent / "Data" / "processed" / "glassdoor_jobs_cleaned.csv"
try:
    df = pd.read_csv(DATA_FILE)
except FileNotFoundError as e:
    raise FileNotFoundError(
        f"Dataset file not found: {DATA_FILE}. Please verify the Data/processed path."
    ) from e


def _get_model_response(prompt: str):
    # sourcery skip: assign-if-exp, reintroduce-else
    if model is None:
        raise RuntimeError(
            "Gemini is not configured. Please set GEMINI_API_KEY in a .env file or the environment."
        )

    if hasattr(model, "generate_content"):
        response = model.generate_content(prompt)
        return response.text if hasattr(response, "text") else str(response)

    if hasattr(model, "generate_text"):
        response = model.generate_text(prompt)
        if hasattr(response, "text"):
            return response.text
        return str(response)

    if hasattr(model, "generate_response"):
        response = model.generate_response(prompt=prompt)
        if hasattr(response, "text"):
            return response.text
        if hasattr(response, "output") and response.output:
            first = response.output[0]
            return getattr(first, "content", str(first))
        return str(response)

    if hasattr(model, "start_chat"):
        response = model.start_chat(messages=[{"role": "user", "content": prompt}])
        if hasattr(response, "response"):
            return getattr(response.response, "content", str(response.response))
        return str(response)

    raise RuntimeError(
        "Gemini model is configured, but no supported generation method was found."
    )


def ask_gemini(question):
    if model is None:
        if GEMINI_API_KEY is None:
            raise RuntimeError(
                "Gemini is not configured. Please set GEMINI_API_KEY in a .env file or the environment."
            )
        raise RuntimeError(
            "Gemini client initialization failed. " \
            f"Last error: {GENAI_INIT_ERROR}"
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

    return _get_model_response(prompt)
