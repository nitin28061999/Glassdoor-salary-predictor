import streamlit as st
from app.gemini_helper import ask_gemini

st.title("🤖 AI Salary Assistant")

st.write(
    "Ask questions related to salary prediction, job roles, industries, or machine learning."
)

question = st.text_area("Enter your question:")

if st.button("Ask AI"):
    if question.strip() == "":
        st.warning("Please enter a question.")
    else:
        try:
            answer = ask_gemini(question)
            st.success(answer)
        except RuntimeError as e:
            st.warning(str(e))
        except Exception as e:
            st.error(f"Error: {e}")
            