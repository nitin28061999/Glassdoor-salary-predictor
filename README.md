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

<img width="1918" height="835" alt="Screenshot 2026-08-20 144439" src="https://github.com/user-attachments/assets/1d1662cf-ca18-4ab5-bb48-8222a4ae3446" />
<img width="1915" height="829" alt="Screenshot 2026-08-20 144508" src="https://github.com/user-attachments/assets/e4486da4-08a8-4321-adc7-757e47593f71" />
<img width="1917" height="804" alt="Screenshot 2026-08-20 144920" src="https://github.com/user-attachments/assets/934eca77-ff1a-49fa-8f9b-bbf8f9897445" />
<img width="1915" height="832" alt="Screenshot 2026-08-20 144936" src="https://github.com/user-attachments/assets/258f1227-5850-444c-9265-d377c8a33054" />
<img width="1912" height="820" alt="Screenshot 2026-08-20 144956" src="https://github.com/user-attachments/assets/31dd79a1-1fc9-4fc0-a52f-da32a88b7fe0" />
<img width="1918" height="820" alt="Screenshot 2026-08-20 145020" src="https://github.com/user-attachments/assets/aed2a818-6ade-4b9b-a0f6-1a70358ce2db" />



## Installation

```bash
pip install -r requirements.txt
streamlit run app/main.py
