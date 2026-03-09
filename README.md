📊 Customer Churn Prediction System

An end-to-end Machine Learning project that predicts whether a customer is likely to churn using XGBoost. 
The model handles class imbalance using SMOTE and is deployed as a Streamlit REST API.


🚀 Project Overview

Customer churn prediction helps businesses identify customers who are likely to stop using their service. 
Retaining customers is significantly more cost-effective than acquiring new ones.

This project:

Performs data preprocessing and feature engineering
Handles class imbalance using SMOTE
Trains an XGBoost classifier
Evaluates performance using ROC-AUC, Precision, Recall
Saves the trained model
Deploys the model using Streamlit API


🛠 Tech Stack

Python
Pandas
NumPy
Scikit-learn
Imbalanced-learn (SMOTE)
XGBoost
Streamlit
Joblib
Matplotlib & Seaborn


## 📂 Project Structure

Churn_model/
│
├── app.py                # Streamlit app for churn prediction
├── requirements.txt      # Python dependencies
├── churn_model.pkl       # Trained ML model
├── scaler.pkl            # Scaler for numeric features
├── columns.pkl           # Saved feature columns
├── venv/                 # Virtual environment (ignored in Git)
└── README.md             # Project documentation
