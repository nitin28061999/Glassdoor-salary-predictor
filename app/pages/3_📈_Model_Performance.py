import streamlit as st
import pandas as pd
from pathlib import Path

st.title("📈 Model Performance")

REPORT_FILE = Path(__file__).resolve().parent.parent.parent / "reports" / "model_results.csv"

if REPORT_FILE.exists():
    results = pd.read_csv(REPORT_FILE)
    st.dataframe(results)

    if "R2" in results.columns and "Model" in results.columns:
        best_model = results.sort_values("R2", ascending=False).iloc[0]
        st.success(
            f"Best Model: {best_model['Model']} (R² = {best_model['R2']:.3f})"
        )
    else:
        st.warning("Model results file is present but missing expected columns.")
else:
    st.warning(
        "Model results are not available. Please add `reports/model_results.csv` or generate it from the model evaluation notebook."
    )