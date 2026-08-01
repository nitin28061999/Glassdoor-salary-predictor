from app.gemini_helper import ask_gemini

question = "What is Machine Learning?"

answer = ask_gemini(question)

print(answer)