from fastapi import FastAPI
from app.schema import CustomerData
from app.model import model, preprocess_input

app = FastAPI()

def encode_input(data):
    encoded = {
        "tenure": data.tenure,
        "MonthlyCharges": data.MonthlyCharges,
        "TotalCharges": data.TotalCharges,
        "SeniorCitizen": data.SeniorCitizen
    }

    encoded["Contract_One year"] = 1 if data.Contract == "One year" else 0
    encoded["Contract_Two year"] = 1 if data.Contract == "Two year" else 0

    encoded["InternetService_Fiber optic"] = 1 if data.InternetService == "Fiber optic" else 0
    encoded["InternetService_No"] = 1 if data.InternetService == "No" else 0

    encoded["PaymentMethod_Electronic check"] = 1 if data.PaymentMethod == "Electronic check" else 0
    encoded["PaymentMethod_Mailed check"] = 1 if data.PaymentMethod == "Mailed check" else 0
    encoded["PaymentMethod_Credit card (automatic)"] = 1 if data.PaymentMethod == "Credit card (automatic)" else 0

    encoded["OnlineSecurity_Yes"] = 1 if data.OnlineSecurity == "Yes" else 0
    encoded["TechSupport_Yes"] = 1 if data.TechSupport == "Yes" else 0
    encoded["PaperlessBilling_Yes"] = 1 if data.PaperlessBilling == "Yes" else 0

    return encoded

@app.get("/")
def home():
    return {"message": "API is running"}

@app.post("/predict")
def predict(data: CustomerData):
    encoded = encode_input(data)
    processed = preprocess_input(encoded)

    prediction = model.predict(processed)[0]
    probability = model.predict_proba(processed)[0][1]

    return {
        "churn_prediction": int(prediction),
        "probability": float(probability)
    }