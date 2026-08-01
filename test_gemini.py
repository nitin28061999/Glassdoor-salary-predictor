from agemini_helper import ask_gemini # pyright: ignore[reportUndefinedVariable, reportUnusedExpression, reportMissingImports]

question = "What is Machine Learning?"

answer = ask_gemini(question)

print(answer)