import streamlit as st
import pandas as pd
import joblib
import os
st.set_page_config(
    page_title="Credit Risk Predictor",
    page_icon="💳",
    layout="centered"
)

st.markdown("""
<style>
.main {
    background-color: #f7f9fc;
}
.title {
    text-align: center;
    color: #1f2937;
}
.subtitle {
    text-align: center;
    color: #6b7280;
    margin-bottom: 30px;
}
.card {
    padding: 25px;
    border-radius: 15px;
    background-color: white;
    box-shadow: 0px 4px 15px rgba(0,0,0,0.08);
}
.stButton>button {
    width: 100%;
    height: 45px;
    border-radius: 10px;
    background-color: #2563eb;
    color: white;
    font-size: 18px;
    font-weight: bold;
}
</style>
""", unsafe_allow_html=True)

st.markdown("<h1 class='title'>💳 Credit Risk Prediction</h1>", unsafe_allow_html=True)
st.markdown(
    "<p class='subtitle'>Predict whether a customer is Good Risk or Bad Risk using ML</p>",
    unsafe_allow_html=True
)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

model_path = os.path.join(
    BASE_DIR,
    "..",
    "models",
    "final_credit_risk_model.pkl"
)

model = joblib.load(model_path)
st.title("Credit Risk Prediction")
st.markdown("<div class='card'>", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    age = st.number_input("Age", 18, 100, 30)
    job = st.selectbox("Job", [0, 1, 2, 3])
    credit_amount = st.number_input("Credit Amount", 100, 20000, 5000)
    duration = st.number_input("Duration (months)", 1, 72, 12)

with col2:
    sex = st.selectbox("Sex", ["male", "female"])
    housing = st.selectbox("Housing", ["own", "rent", "free"])
    saving = st.selectbox(
        "Saving Accounts",
        ["little", "moderate", "rich", "quite rich", "unknown"]
    )
    checking = st.selectbox(
        "Checking Account",
        ["little", "moderate", "rich", "unknown"]
    )
    purpose = st.selectbox(
        "Purpose",
        ["car", "radio/TV", "furniture/equipment", "education", "business"]
    )

st.markdown("</div>", unsafe_allow_html=True)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

columns = joblib.load(
    os.path.join(BASE_DIR, "..", "models", "columns.pkl")
)
if st.button("Predict Risk"):

    input_df = pd.DataFrame(
    [[0] * len(columns)],
    columns=columns
)

    pred = model.predict(input_df)

    if pred[0] == 1:
        st.success("✅ Good Credit Risk")
        st.balloons()
    else:
        st.error("⚠️ Bad Credit Risk")
