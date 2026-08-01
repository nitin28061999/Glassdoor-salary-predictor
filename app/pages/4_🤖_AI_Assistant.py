import streamlit as st
from gemini_helper import ask_gemini

st.title("🤖 AI Salary Assistant")

st.write("Ask questions about salary trends, job roles, industries, or the project.")

question = st.text_area(
    "Enter your question"
)

if st.button("Ask AI"):

    if question.strip() == "":
        st.warning("Please enter a question.")
    else:

        answer = ask_gemini(question)

        st.success(answer)