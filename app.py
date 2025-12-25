import streamlit as st
import pickle
import time

# Load model
@st.cache_resource
def load_model():
    with open("calorie_tracker.pkl", "rb") as f:
        return pickle.load(f)

model = load_model()

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
duration = st.number_input("⏱ Workout Duration (minutes)", min_value=0, step=1)
age = st.number_input("🎂 Age (years)", min_value=0, step=1)
height = st.number_input("📏 Height (cm)", min_value=0, step=1)
weight = st.number_input("⚖️ Weight (kg)", min_value=0, step=1)
gender_ui = st.selectbox("🚻 Gender", ["Male", "Female"])
gender = 1 if gender_ui == "Male" else 0
body_temp = st.number_input(
    "🌡️ Body Temperature (°C)",
    min_value=34.0,
    max_value=42.0,
    value=36.5,
    step=0.1
)

st.markdown("</div>", unsafe_allow_html=True)



col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    if st.button('🔥 Calculate Calories Burnt'):

       
        if (
            heart_rate < 40 or heart_rate > 200 or
            duration <= 0 or
            age < 18 or age > 80 or
            height < 120 or height > 200 or
            weight < 38 or weight > 150 or
            body_temp < 34 or body_temp > 42    
        ):
            st.warning("⚠ Please enter valid data in all fields.")
        else:
            
            calorie_burned = model.predict(
                [[heart_rate, duration, age, height, weight, gender,body_temp]]
            )[0]

            with st.spinner('Calculating... please wait ⏳'):
                placeholder = st.empty()
                time.sleep(0.5)

                placeholder.markdown(
                    f"""
                    <div class='result-container' style="color: #00ff99;">
                    🔥 Calories Burned<br>
                    <span style="color: #00ff99; font-size: 2.5rem; font-weight: bold;">
                    {calorie_burned:.2f}
                </span>
                </div>
                """,
                    unsafe_allow_html=True
                )

