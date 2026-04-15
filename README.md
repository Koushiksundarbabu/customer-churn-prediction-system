# 🚀 Customer Churn Prediction System

An end-to-end machine learning system that predicts whether a customer is likely to churn, deployed with a FastAPI backend and Streamlit frontend.

---

## 📊 Problem Statement

Customer churn is a critical problem for businesses. Predicting churn helps companies take proactive actions to retain customers and reduce revenue loss.

---

## 🧠 Model Development

- Performed data preprocessing and feature engineering  
- Handled categorical variables using encoding  
- Addressed class imbalance using `scale_pos_weight`  
- Trained multiple models:
  - Logistic Regression  
  - Random Forest  
  - XGBoost  

### 🏆 Best Model: XGBoost

### 📈 Performance Metrics

- Accuracy: **74%**  
- Precision (Churn): **0.51**  
- Recall (Churn): **0.79**  
- F1 Score (Churn): **0.62**  
- ROC-AUC: **0.83**

💡 **Insight:**  
Recall is prioritized in churn prediction since identifying customers likely to leave is more valuable than minimizing false positives.

---

## ⚙️ System Architecture
User → Streamlit UI → FastAPI API → ML Model → Prediction → UI


---

## 🔧 Backend (FastAPI)

- Built REST API using FastAPI  
- Endpoint: `/predict`  
- Input validation using Pydantic  
- Loads trained model (`.pkl`) and feature columns  
- Returns prediction + probability  

### 🌐 API Docs  
👉 https://churn-api-h2rp.onrender.com/docs

---

## 🎨 Frontend (Streamlit)

- Interactive UI for user input  
- Sends POST request to FastAPI  
- Displays prediction with probability  
- Clean and user-friendly interface  

### 🌐 Live App  
👉 [Add your Streamlit link here]

---

## 🛠 Tech Stack

- Python  
- Pandas, NumPy  
- Scikit-learn, XGBoost  
- FastAPI  
- Streamlit  
- Render (Backend Deployment)  
- Streamlit Cloud (Frontend Deployment)

---

## 🚀 Deployment

- Backend deployed on Render  
- Frontend deployed on Streamlit Cloud  
- Integrated via REST API for real-time predictions  

---

## 💡 Key Learnings

- Building end-to-end ML systems  
- Deploying ML models as APIs  
- Integrating frontend with backend  
- Handling real-world issues like API errors and deployment challenges  

---

## 📌 Future Improvements

- Add authentication system  
- Improve UI/UX  
- Add model monitoring  
- Deploy using Docker  

---

## 👨‍💻 Author

Koushik
