import streamlit as st

# 🔥 MUST BE FIRST STREAMLIT COMMAND
st.set_page_config(
    page_title="Calorie Tracker 🔥",
    page_icon="🔥",
    layout="centered"
)

import pickle
import time
import math

# ---------------- LOAD MODEL ----------------
@st.cache_resource
def load_model():
    with open("calorie_tracker.pkl", "rb") as f:
        return pickle.load(f)

model = load_model()

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>
body {
    background: linear-gradient(135deg, #0f0c29, #302b63, #24243e);
}
.circle {
    width: 200px;
    height: 200px;
    border-radius: 50%;
    border: 12px solid rgba(255,255,255,0.2);
    display: flex;
    align-items: center;
    justify-content: center;
    margin: auto;
    font-size: 2.3rem;
    font-weight: bold;
    color: #ff7e5f;
    box-shadow: 0 0 30px rgba(255,126,95,0.6);
}
</style>
""", unsafe_allow_html=True)

# ---------------- TITLE ----------------
st.markdown("<h1 style='text-align:center;color:#ff7e5f;'>🔥 Calorie Burn Predictor</h1>", unsafe_allow_html=True)

# ---------------- INPUTS ----------------
heart_rate = st.number_input("💓 Heart Rate (bpm)", min_value=40, max_value=200, step=1)
duration = st.number_input("⏱ Workout Duration (minutes)", min_value=1, max_value=300, step=1)
age = st.number_input("🎂 Age (years)", min_value=18, max_value=80, step=1)
height = st.number_input("📏 Height (cm)", min_value=120, max_value=220, step=1)
weight = st.number_input("⚖️ Weight (kg)", min_value=30, max_value=200, step=1)
body_temp = st.number_input("🌡 Body Temperature (°C)", min_value=35.0, max_value=42.0, step=0.1)

gender_ui = st.selectbox("🚻 Gender", ["Male", "Female"])
gender = 1 if gender_ui == "Male" else 0

# ---------------- BUTTON ----------------
if st.button("🔥 Calculate Calories Burnt"):
    with st.spinner("Calculating calories... ⏳"):
        time.sleep(0.5)

        # MODEL INPUT (ORDER MUST MATCH TRAINING)
        features = [[
            heart_rate,
            duration,
            age,
            height,
            weight,
            body_temp,
            gender
        ]]

        calorie_burned = model.predict(features)[0]
        calorie_burned = max(0, calorie_burned)

        # ---------------- CIRCULAR ANIMATION ----------------
        placeholder = st.empty()
        steps = 60

        for i in range(steps + 1):
            value = (calorie_burned / steps) * i
            placeholder.markdown(
                f"""
                <div class="circle">
                     {value:.0f}
                </div>
                """,
                unsafe_allow_html=True
            )
            time.sleep(0.02)

        # FINAL VALUE
        placeholder.markdown(
            f"""
            <div class="circle">
                 {calorie_burned:.2f}
            </div>
            """,
            unsafe_allow_html=True
        )

        
