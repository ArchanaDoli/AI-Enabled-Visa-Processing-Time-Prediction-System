import streamlit as st
from predict import predict_processing_time

st.title("Visa Processing Time Predictor")

country = st.selectbox("Country", ["India","USA","UK","Canada","France","Germany"])
visa_type = st.selectbox("Visa Type", ["Tourist","Work","Student"])
office = st.selectbox("Processing Office", ["Hyderabad","London","New Delhi","Sydney","Toronto"])
month = st.slider("Application Month", 1, 12)

if st.button("Predict Processing Time"):

    input_data = {
        "country": country,
        "visa_type": visa_type,
        "office": office,
        "month": month
    }

    result = predict_processing_time(input_data)

    st.success(f"Estimated Processing Time: {result} days")