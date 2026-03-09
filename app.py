import streamlit as st
import pandas as pd
import joblib

# Load files
model = joblib.load("churn_model.pkl")
scaler = joblib.load("scaler.pkl")
columns = joblib.load("columns.pkl")

st.title("Customer Churn Prediction")

tenure = st.number_input("Tenure (months)", 0, 72)
monthly_charges = st.number_input("Monthly Charges", 0.0, 200.0)
total_charges = st.number_input("Total Charges", 0.0, 10000.0)

if st.button("Predict"):

    input_data = pd.DataFrame({
        "tenure":[tenure],
        "MonthlyCharges":[monthly_charges],
        "TotalCharges":[total_charges]
    })

    input_data = input_data.reindex(columns=columns, fill_value=0)

    input_scaled = scaler.transform(input_data)

    prediction = model.predict(input_scaled)[0]

    if prediction == 1:
        st.error("Customer is likely to churn")
    else:
        st.success("Customer will stay")