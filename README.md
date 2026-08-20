# Glassdoor Salary Prediction

## Business Problem

Predict employee salaries using machine learning.

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Streamlit
- Plotly
- Google Gemini API

## Machine Learning Models

- Linear Regression
- Decision Tree
- Random Forest
- Gradient Boosting

## Features

- Salary Prediction
- Interactive Dashboard
- Exploratory Data Analysis
- AI Assistant using Gemini

## Folder Structure

Glassdoor-salary-predictor/
│
├── app/
│   ├── app.py
│   └── components/
│       └── ...
│
├── data/
│   ├── raw/
│   │   └── glassdoor_raw.csv
│   └── processed/
│       └── glassdoor_cleaned.csv
│
├── models/
│   ├── linear_regression.pkl
│   ├── decision_tree.pkl
│   ├── random_forest.pkl
│   └── gradient_boosting.pkl
│
├── notebooks/
│   ├── 01_data_cleaning.ipynb
│   ├── 02_exploratory_data_analysis.ipynb
│   ├── 03_feature_engineering.ipynb
│   └── 04_model_training.ipynb
│
├── src/
│   ├── data_preprocessing.py
│   ├── feature_engineering.py
│   ├── train.py
│   ├── predict.py
│   └── evaluate.py
│
├── reports/
│   ├── model_comparison.csv
│   └── figures/
│       ├── salary_distribution.png
│       ├── experience_vs_salary.png
│       └── feature_importance.png
│
├── images/
│   ├── app_home.png
│   ├── prediction.png
│   └── dashboard.png
│
├── .gitignore
├── requirements.txt
├── README.md
└── LICENSE

## Screenshots



## Installation

```bash
pip install -r requirements.txt
streamlit run app/main.py
