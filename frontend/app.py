import streamlit as st
import requests

# Page config
st.set_page_config(
    page_title="Churn Prediction",
    page_icon="📊",
    layout="wide"
)

# Custom CSS
st.markdown("""
    <style>
    .main {
        background-color: #f5f7fa;
    }
    .stButton>button {
        background-color: #1f77b4;
        color: white;
        border-radius: 10px;
        height: 3em;
        width: 100%;
        font-size: 16px;
    }
    </style>
""", unsafe_allow_html=True)

# Title
st.markdown("""
# 📊 Customer Churn Prediction
Predict whether a customer is likely to churn based on their profile.
""")

st.markdown("---")

st.subheader("📋 Customer Information")

# Create columns
col1, col2 = st.columns(2)

# LEFT COLUMN
with col1:
    tenure = st.slider("Tenure (in months)", 0, 72, 12)
    monthly = st.number_input("Monthly Charges", 0.0, 200.0, 50.0)
    total = st.number_input("Total Charges", 0.0, 10000.0, 500.0)
    contract = st.selectbox("Contract", ["Month-to-month", "One year", "Two year"])
    internet = st.selectbox("Internet Service", ["DSL", "Fiber optic", "No"])

# RIGHT COLUMN
with col2:
    payment = st.selectbox("Payment Method", [
        "Electronic check", "Mailed check",
        "Bank transfer (automatic)", "Credit card (automatic)"
    ])

    security = st.selectbox("Online Security", ["No", "Yes"])
    support = st.selectbox("Tech Support", ["No", "Yes"])
    paperless = st.selectbox("Paperless Billing", ["No", "Yes"])

    senior = st.selectbox("Senior Citizen", ["No", "Yes"])
    senior_value = 1 if senior == "Yes" else 0

st.markdown("---")

# Predict button
if st.button("🔍 Predict Churn"):

    data = {
        "tenure": tenure,
        "MonthlyCharges": monthly,
        "TotalCharges": total,
        "SeniorCitizen": senior_value,
        "Contract": contract,
        "InternetService": internet,
        "PaymentMethod": payment,
        "OnlineSecurity": security,
        "TechSupport": support,
        "PaperlessBilling": paperless
    }

    try:
        response = requests.post(
            "https://churn-api-h2rp.onrender.com/predict",
            json=data
        )

        result = response.json()

        st.markdown("### 📊 Prediction Result")

        if result["churn_prediction"] == 1:
            st.markdown(f"""
            <div style='background-color:#ffe6e6;padding:20px;border-radius:10px'>
            ⚠️ <b>High Risk of Churn</b><br>
            Probability: {result['probability']:.2f}
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown(f"""
            <div style='background-color:#e6ffe6;padding:20px;border-radius:10px'>
            ✅ <b>Customer Likely to Stay</b><br>
            Probability: {result['probability']:.2f}
            </div>
            """, unsafe_allow_html=True)

    except:
        st.error("⚠️ Unable to connect to backend. Make sure FastAPI is running.")