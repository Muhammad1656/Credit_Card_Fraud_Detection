import streamlit as st
import pandas as pd
import joblib
import time

# 1. Page Config & CSS
st.set_page_config(page_title="AI Fraud Shield", page_icon="🛡️", layout="centered")
st.markdown("""
<style>
    /* --- AWESOME BACKGROUND --- */
    .stApp {
        background: linear-gradient(135deg, #0b0c10 0%, #1f2833 100%);
    }

    /* --- THE GLOWING MAIN TITLES --- */
    .glowing-title { 
        font-size: 3.5em; 
        font-weight: 900; 
        text-align: center; 
        background: linear-gradient(90deg, #FF416C, #FF4B2B, #FF416C);
        background-size: 200% auto; 
        color: transparent; 
        -webkit-background-clip: text; 
        animation: shine 3s linear infinite;
        margin-bottom: 0px; 
        text-shadow: 0px 5px 15px rgba(255, 65, 108, 0.4);
    }
    @keyframes shine { to { background-position: 200% center; } }
    .subtitle { text-align: center; color: #66fcf1; font-style: italic; margin-bottom: 40px; font-weight: bold; letter-spacing: 1px;}
    
    /* --- ATTRACTIVE SECTION HEADINGS --- */
    .section-header {
        font-size: 1.8em;
        font-weight: 700;
        color: #ffffff;
        text-transform: uppercase;
        letter-spacing: 2px;
        border-bottom: 2px solid #45a29e;
        padding-bottom: 10px;
        margin-top: 30px;
        margin-bottom: 20px;
        text-shadow: 0 0 10px rgba(69, 162, 158, 0.8);
        display: inline-block;
    }

    /* --- BUTTON STYLING --- */
    div.stButton > button { 
        border: 2px solid #FF416C; color: #FF416C; border-radius: 12px; padding: 10px; width: 100%; 
        transition: all 0.3s ease-in-out; font-weight: bold; font-size: 1.1em;
    }
    div.stButton > button:hover { 
        background-color: #FF416C; color: white; 
        transform: translateY(-5px); 
        box-shadow: 0 10px 20px rgba(255, 65, 108, 0.6);
    }

    /* --- MAGIC BOXES: MOVING LIGHT OUTLINE & HOVER IGNITE --- */
    @keyframes pulse-border {
        0% { box-shadow: 0 0 0px #45a29e, inset 0 0 0px #45a29e; border: 1px solid rgba(69, 162, 158, 0.2); }
        50% { box-shadow: 0 0 8px #45a29e, inset 0 0 2px #45a29e; border: 1px solid rgba(69, 162, 158, 0.8); }
        100% { box-shadow: 0 0 0px #45a29e, inset 0 0 0px #45a29e; border: 1px solid rgba(69, 162, 158, 0.2); }
    }

    div[data-testid="stNumberInput"], div[data-testid="stSlider"] {
        transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275); /* Bouncy smooth transition */
        padding: 10px;
        border-radius: 12px;
        background: rgba(11, 12, 16, 0.6); /* Dark base */
        animation: pulse-border 2.5s infinite alternate; /* Background mein light chalti rahegi */
    }
    
    /* Jaise hi mouse paas aaye: Hawa mein urey aur poori light jal jaye */
    div[data-testid="stNumberInput"]:hover, div[data-testid="stSlider"]:hover {
        transform: translateY(-10px); /* 10 pixels hawa mein */
        animation: none; /* Pulse stop */
        border: 1px solid #66fcf1; /* Neon border */
        box-shadow: 0 15px 30px rgba(0, 0, 0, 0.6), 0 0 20px #66fcf1, inset 0 0 10px #66fcf1 !important; /* Glow light */
        background: rgba(102, 252, 241, 0.05); /* Ander se bhi chamkega */
    }
</style>
""", unsafe_allow_html=True)

st.markdown('<p class="glowing-title">🛡️ AI FRAUD SHIELD PRO</p>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Neural Network Monitoring System • Built by Muhammad Bin Nadeem</p>', unsafe_allow_html=True)

# 2. Load the NEW 5-Feature Brain
@st.cache_resource
def load_models():
    return joblib.load('random_forest_fraud_model.pkl'), joblib.load('data_scaler.pkl')

try:
    model, scaler = load_models()
except:
    st.error("❌ Neural Brain missing! Pehle main.py run karo."); st.stop()

# 3. Security Settings (Attractive Heading)
st.markdown('<div class="section-header">⚙️ Bank Security Settings</div>', unsafe_allow_html=True)
threshold = st.slider("AI Strictness Level (Risk Threshold %)", 5, 90, 30, 5)
st.markdown("---")

# 4. Input Section (PURE REALITY - Attractive Heading)
st.markdown('<div class="section-header">📡 Enter Transaction Telemetry</div>', unsafe_allow_html=True)
amount = st.number_input("💰 Transaction Amount ($)", min_value=0.0, value=150.00, step=10.0)

col1, col2 = st.columns(2)
with col1:
    v14 = st.number_input("V14 (Risk Factor Alpha)", value=0.0)
    v4 = st.number_input("V4 (Risk Factor Beta)", value=0.0)
with col2:
    v10 = st.number_input("V10 (Risk Factor Gamma)", value=0.0)
    v12 = st.number_input("V12 (Risk Factor Delta)", value=0.0)

st.markdown("<br>", unsafe_allow_html=True)

# 5. The Real AI Scan (No Cheat Codes)
if st.button("EXECUTE DEEP SECURITY SCAN"):
    progress = st.progress(0); time.sleep(0.2); progress.progress(100); progress.empty()
    
    # Amount ko scale karna
    scaled_amount = scaler.transform([[amount]])[0][0]
    
    # 🔥 THE FIX: AI ko exactly wahi 5 cheezein dena jis par wo train hua hai (Sequence same hona chahiye)
    # Sequence: ['V14', 'V4', 'V10', 'V12', 'Amount']
    input_df = pd.DataFrame([[v14, v4, v10, v12, scaled_amount]], 
                            columns=['V14', 'V4', 'V10', 'V12', 'Amount'])
    
    # AI Prediction
    pred_prob = model.predict_proba(input_df)[0]
    risk_score = int(pred_prob[1] * 100)
    
    st.markdown(f"### 📊 Fraud Risk Score: {risk_score}%")
    st.progress(risk_score / 100)
    
    if risk_score >= threshold:
        st.error(f"🚨 **FRAUD DETECTED!** AI is {risk_score}% sure this is a fraudulent pattern.")
    else:
        st.success(f"✅ **TRANSACTION VERIFIED!** Risk score ({risk_score}%) is below bank threshold.")