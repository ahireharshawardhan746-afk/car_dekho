import pandas as pd
import numpy as np
import streamlit as st
import pickle


# Load the saved model
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)



# UI inputs
avg_session = st.number_input("Avg. Session Length")
time_app = st.number_input("Time on App")
time_web = st.number_input("Time on Website")
membership = st.number_input("Length of Membership")

# Predict
if st.button("Predict"):
    prediction = model.predict(
        [[avg_session, time_app, time_web, membership]]
    )
    st.success(f"Predicted Yearly Amount Spent: ${prediction[0]:.2f}")