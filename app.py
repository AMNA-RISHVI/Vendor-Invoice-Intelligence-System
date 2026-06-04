import streamlit as st
import pandas as pd
from inference.predict_freight import predict_freight_cost
from inference.predict_invoice_flag import predict_invoice_flag 
from inference.predict_freight import load_model as load_freight_model
import joblib

freight_scaler = joblib.load("models/scaler.pkl")

# --- UI CONFIG ---
st.set_page_config(page_title="Vendor Invoice Intelligence Portal", page_icon="🧾", layout="wide")

# --- CUSTOM CSS FOR "Glassmorphism Purple Gradient" THEME ---
st.markdown("""
<style>

/* --- MAIN BACKGROUND (Gradient + Blur Effect) --- */
.stApp {
    background: linear-gradient(135deg, #1a1a2e, #16213e, #0f3460);
    color: #EAEAEA;
}

/* --- HEADER STYLE --- */
h1 {
    font-family: 'Poppins', sans-serif;
    font-weight: 800;
    color: #E94560 !important;
    letter-spacing: 1px;
}

/* --- SIDEBAR (GLASS EFFECT) --- */
[data-testid="stSidebar"] {
    background: rgba(255, 255, 255, 0.05);
    backdrop-filter: blur(12px);
    border-right: 1px solid rgba(255,255,255,0.1);
}

/* --- BUTTON STYLE (GRADIENT + ANIMATION) --- */
div.stButton > button:first-child {
    background: linear-gradient(45deg, #ff4e50, #fc913a);
    color: white;
    border-radius: 12px;
    border: none;
    padding: 0.6em;
    font-weight: bold;
    transition: 0.3s ease;
    width: 100%;
}

/* Hover Effect */
div.stButton > button:hover {
    transform: scale(1.05);
    background: linear-gradient(45deg, #fc913a, #ff4e50);
    box-shadow: 0 0 20px rgba(255, 78, 80, 0.6);
}

/* --- INPUT FIELDS --- */
input, .stNumberInput input {
    border-radius: 10px !important;
    border: 1px solid rgba(255,255,255,0.2) !important;
    background-color: rgba(255,255,255,0.05) !important;
    color: white !important;
}

/* --- METRICS --- */
[data-testid="stMetricValue"] {
    color: #00F5D4;
    font-size: 28px;
    font-weight: bold;
}

/* --- CARDS (ADD DEPTH) --- */
.block-container {
    padding: 2rem;
    border-radius: 15px;
}

/* --- SUCCESS / ERROR COLORS --- */
.stAlert {
    border-radius: 10px;
}

</style>
""", unsafe_allow_html=True)

# --- SIDEBAR NAVIGATION ---
with st.sidebar:
    st.title("⚙️ Control Panel")
    app_mode = st.radio("Navigation", ["Freight Prediction", "Risk Analysis"])
    st.markdown("---")
    st.info("""
    **Intelligence Metrics:**
    * 🚀 Logistics Optimization
    * 🛡️ Fraud Guard AI
    * 📊 Financial Precision
    """)

# --- MAIN HEADER ---
st.title("🧾Vendor Invoice Intelligence Portal")
st.markdown("#### *AI-powered decision support for finance and logistics.*")
st.divider()

# --- APP LOGIC ---

if app_mode == "Freight Prediction":
    st.subheader("📦 Forecast Freight Expenditure")
    col1, col2 = st.columns(2)
    with col1:
        quantity = st.number_input("Item Quantity", min_value=1, value=10)
    with col2:
        dollars = st.number_input("Invoice Total ($)", min_value=1.0, value=500.0)

    if st.button("✨ Calculate Expected Freight"):

        try:
            # Load model to get expected features
            model = load_freight_model()
            expected_cols = model.feature_names_in_

            # Create base input
            input_dict = {
                "invoice_quantity": quantity,
                "invoice_dollars": dollars
            }

            # Convert to DataFrame
            input_df = pd.DataFrame([input_dict])

            # CRITICAL FIX: match model features
            input_df = input_df.reindex(columns=expected_cols, fill_value=0)

            # ✅ Load scaler
            freight_scaler = joblib.load("models/scaler.pkl")

            # ✅ Scale input
            scaled_values = freight_scaler.transform(input_df)

            # Convert back to DataFrame (keep column names)
            scaled_df = pd.DataFrame(scaled_values, columns=input_df.columns)

            # ✅ Now call prediction with scaled data
            result_df = predict_freight_cost(scaled_df.to_dict(orient="list"))

            if result_df is not None:
                prediction = result_df['Predicted_Freight'].iloc[0]
                st.metric(label="Calculated Freight Cost", value=f"${prediction:,.2f}")
                st.balloons()

        except Exception as e:
            st.error(f"Prediction Error: {e}")

elif app_mode == "Risk Analysis":
    st.subheader("🚩 Invoice Risk Profiler")
    col1, col2 = st.columns(2)
    with col1:
        inv_qty = st.number_input("Invoice Quantity", min_value=1, value=50)
        inv_dlrs = st.number_input("Invoice Dollars ($)", min_value=1.0, value=1200.0)
        freight = st.number_input("Freight Component ($)", min_value=0.0, value=45.0)
    
    with col2:
        item_qty = st.number_input("Total Item Quantity", min_value=1, value=50)
        item_dlrs = st.number_input("Total Item Dollars ($)", min_value=1.0, value=1195.0)
    
    st.markdown("---")
    if st.button("🔍 Run AI Risk Assessment"):
        input_risk = {
            "invoice_quantity": [inv_qty],
            "invoice_dollars": [inv_dlrs],
            "Freight": [freight],
            "total_item_quantity": [item_qty],
            "total_item_dollars": [item_dlrs]
        }
        
        risk_result = predict_invoice_flag(input_risk)
        
        if risk_result is not None:
            is_flagged = risk_result['Predicted_Flag'].iloc[0]
            
            if is_flagged == 1:
                st.error("🚨 **HIGH RISK**: Manual review required.")
            else:
                st.success("✅ **LOW RISK**: Invoice cleared for processing.")
