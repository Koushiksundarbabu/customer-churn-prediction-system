from pydantic import BaseModel

class CustomerData(BaseModel):
    tenure: int
    MonthlyCharges: float
    TotalCharges: float
    SeniorCitizen: int

    Contract: str
    InternetService: str
    PaymentMethod: str
    OnlineSecurity: str
    TechSupport: str
    PaperlessBilling: str