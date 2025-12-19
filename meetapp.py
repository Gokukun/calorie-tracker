import streamlit as st
import joblib
import time

# Load model
calorie_burned_model = joblib.load("meet_project_joblib")

# --- Custom CSS: Glassmorphism + Better UI ---
st.markdown("""
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;600&display=swap" rel="stylesheet">
    <style>
    html, body, [class*="css"]  {
        font-family: 'Poppins', sans-serif;
        background: linear-gradient(135deg, #0f0c29, #302b63, #24243e);
        color: white;
    }
    h1 {
        color: #FF6B6B;
        text-align: center;
        font-weight: 700;
        margin-bottom: 1rem;
    }
    .stButton>button {
        display: block;
        margin: 0 auto;
        background: linear-gradient(90deg, #ff7e5f, #feb47b);
        color: white;
        border: none;
        border-radius: 50px;
        padding: 0.75em 2em;
        font-size: 1.1em;
        font-weight: bold;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(255, 126, 95, 0.4);
    }
    .stButton>button:hover {
        transform: scale(1.05);
        box-shadow: 0 6px 20px rgba(255, 126, 95, 0.6);
    }

    .result-container {
        margin-top: 3rem;
        padding: 30px;
        background: rgba(255, 255, 255, 0.1);
        box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.37);
        border-radius: 20px;
        text-align: center;
        font-size: 2rem;
        font-weight: bold;
        color: #ffffff;
        backdrop-filter: blur(10px);
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h1>Calorie Tracker 🔥</h1>", unsafe_allow_html=True)


st.markdown("<div class='input-container'>", unsafe_allow_html=True)
heart_rate = st.number_input("💓 Enter your heart rate", value=0, step=1)
duration = st.number_input("⏱ Enter your workout duration (minutes)", value=0, step=1)
st.markdown("</div>", unsafe_allow_html=True)


col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    if st.button('🔥 Calculate Calories Burnt'):
        if heart_rate <= 0 or duration <= 0:
            st.warning("⚠ Please enter valid heart rate and duration values greater than 0.")
        else:
            calorie_burned = calorie_burned_model.predict([[heart_rate, duration]])[0]
            with st.spinner('Calculating... please wait ⏳'):
                placeholder = st.empty()
                max_val = int(calorie_burned)
                step = max(1, abs(max_val) // 100)
                start = 0 if calorie_burned >= 0 else max_val

                for i in range(start, max_val + 1, step):
                    placeholder.markdown(
                        f"<div class='result-container'>Calories Burned = {i}</div>",
                        unsafe_allow_html=True
                    )
                    time.sleep(0.01)

                # Final result
                placeholder.markdown(
                    f"<div class='result-container'>Calories Burnt  {calorie_burned:.2f}</div>",
                    unsafe_allow_html=True
                )