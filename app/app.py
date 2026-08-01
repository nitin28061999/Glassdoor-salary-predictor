import streamlit as st

from predictor import predict_salary

from eda import *

from utils import *

st.set_page_config(
    page_title="Glassdoor Salary Predictor",
    layout="wide"
)

st.title("💼 Glassdoor Salary Prediction")

st.sidebar.title("Navigation")

page = st.sidebar.radio(
    "Go To",
    [
        "Home",
        "EDA",
        "Predict Salary"
    ]
)