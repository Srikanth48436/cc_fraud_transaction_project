import streamlit as st
import joblib
import numpy as np

model = joblib.load("models/xgb_model.pkl")
scaler = joblib.load("models/scaler.pkl")

st.title("💳 Credit Card Fraud Detection")

amount = st.number_input("Transaction Amount")
time = st.number_input("Transaction Time")

if st.button("Predict"):
    features = np.zeros((1,30))
    features[0][0] = time
    features[0][1] = amount

    features = scaler.transform(features)

    prediction = model.predict(features)

    if prediction == 1:
        st.error("⚠️ Fraudulent Transaction")
    else:
        st.success("✅ Legit Transaction")
