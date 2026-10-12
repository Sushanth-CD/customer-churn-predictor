import streamlit as st
import joblib
import pandas as pd

# Categorical

model = joblib.load("customer_churn_model.pkl")
st.title("Customer Churn Predictor")

gender = st.selectbox(
    "Gender",
    ["Female", "Male"]
)

partner = st.selectbox(
    "Partner",
    ["Yes", "No"]
)

contract = st.selectbox(
    "Contract",
    ["Month-to-month", "One year", "Two year"]
)

dependents = st.selectbox(
    "Dependents",
    ["Yes", "No"]
)

phone_service = st.selectbox(
    "Phone Service",
    ["Yes", "No"]
)

paperless_billing = st.selectbox(
    "Paperless Billing",
    ["Yes", "No"]
)

multiple_lines = st.selectbox(
    "Multiple Lines",
    ["Yes", "No", "No phone service"]
)

internet_service = st.selectbox(
    "Internet Service",
    ["DSL", "Fiber Optic", "No"]
)

online_security = st.selectbox(
    "Online Security",
    ["Yes", "No", "No internet service"]
)

online_backup = st.selectbox(
    "Online Backup",
    ["Yes", "No", "No internet service"]
)

device_protection = st.selectbox(
    "Device Protection",
    ["Yes", "No", "No internet service"]
)

tech_support = st.selectbox(
    "Tech Support",
    ["Yes", "No", "No internet service"]
)

streaming_tv = st.selectbox(
    "Streaming TV",
    ["Yes", "No", "No internet service"]
)

streaming_movies = st.selectbox(
    "Streaming Movies",
    ["Yes", "No", "No internet service"]
)

payment_method = st.selectbox(
    "Payment Method",
    ["Electronic check", "Mailed check", "Bank transfer (automatic)", "Credit card (automatic)"]
)

# Numerical

senior_citizen = st.selectbox(
    "Senior Citizen",
    [0, 1]
)

tenure = st.number_input(
    "Tenure",
    min_value=0,
    max_value=72,
    step=1
)

monthly_charges = st.number_input(
    "Monthly Charges",
    min_value=18.25,
    max_value=118.75,
)

num_Admin_Tickets = st.number_input(
    "Num admin tickets",
    min_value=0,
    max_value=5,
    step=1
)

num_Tech_Tickets  = st.number_input(
    "Num tech tickets",
    min_value=0,
    max_value=9,
    step=1
)

total_charges = st.number_input(
    "Total Charges",
    min_value=0.00,
    max_value=8684.80,
)

customer_data = {
    "gender": gender,
    "SeniorCitizen": senior_citizen,
    "Partner": partner,
    "Dependents": dependents,
    "tenure": tenure,
    "PhoneService": phone_service,
    "MultipleLines": multiple_lines,
    "InternetService": internet_service,
    "OnlineSecurity": online_security,
    "OnlineBackup": online_backup,
    "DeviceProtection": device_protection,
    "TechSupport": tech_support,
    "StreamingTV": streaming_tv,
    "StreamingMovies": streaming_movies,
    "Contract": contract,
    "PaperlessBilling": paperless_billing,
    "PaymentMethod": payment_method,
    "MonthlyCharges": monthly_charges,
    "TotalCharges": total_charges,
    "numAdminTickets": num_Admin_Tickets,
    "numTechTickets": num_Tech_Tickets
}

customer_df = pd.DataFrame([customer_data])

if st.button("Predict Churn"):
    probability = model.predict_proba(customer_df)[:, 1][0]

    prediction = "Yes" if probability >= 0.35 else "No"

    st.write(f"Churn Probability: {probability:.2%}")
    st.write(f"Prediction: {prediction}")