import joblib
import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
model = joblib.load(BASE_DIR / "models" / "random_forest_model.pkl")
columns = joblib.load(BASE_DIR / "models" / "model_columns.pkl")


def predict_salary(user_input):
    input_df = pd.DataFrame([user_input])

    input_df = pd.get_dummies(input_df)

    input_df = input_df.reindex(columns=columns, fill_value=0)

    prediction = model.predict(input_df)

    return prediction[0]