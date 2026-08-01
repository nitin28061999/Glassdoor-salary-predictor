import streamlit as st
import pandas as pd

st.title("📈 Model Performance")

results = pd.read_csv("../reports/model_results.csv")

st.dataframe(results)

best_model = results.sort_values("R2", ascending=False).iloc[0]

st.success(
    f"Best Model: {best_model['Model']} (R² = {best_model['R2']:.3f})"
)