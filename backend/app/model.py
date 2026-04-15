import joblib
import pandas as pd

model = joblib.load("churn_model.pkl")
columns = joblib.load("columns.pkl")

def preprocess_input(data: dict):
    df = pd.DataFrame([data])

    for col in columns:
        if col not in df.columns:
            df[col] = 0

    df = df[columns]
    return df