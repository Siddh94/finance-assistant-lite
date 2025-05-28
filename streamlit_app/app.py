import streamlit as st
import requests
import tempfile

st.set_page_config(page_title="📈 Finance Assistant", layout="centered")
st.title("📊 AI-Powered Market Briefing")

BACKEND_URL = "http://localhost:8000"

# 🧪 Toggle for demo mode
DEMO_MODE = st.sidebar.toggle("🧪 Demo Mode (no API calls)", value=False)

# --- Stock Groups ---
stock_groups = {
    "Asia Tech (TSMC, Samsung)": ["TSM", "005930.KQ"],
    "US Tech (Apple, Nvidia)": ["AAPL", "NVDA"],
    "Banking (JPM, HDFC)": ["JPM", "HDFCBANK.BO"]
}

# --- Suggested Questions ---
default_questions = [
    "What’s our risk exposure today?",
    "Any earnings surprises this week?",
    "Summarize key changes in allocation.",
    "Where should I reduce investment?"
]

mode = st.radio("Choose Input Mode", ["Text", "Voice"])

# --- TEXT MODE ---
if mode == "Text":
    group = st.selectbox("Select a stock group:", list(stock_groups.keys()))
    symbols = stock_groups[group]
    query = st.selectbox("Choose a question:", default_questions)

    if st.button("Get Market Briefing"):
        with st.spinner("Thinking..."):
            try:
                if DEMO_MODE:
                    data = {
                        "summary": "🧪 [Demo] Asia tech allocation is 18%. TSMC beat expectations by 15%, Samsung missed slightly. Market sentiment: neutral to optimistic."
                    }
                else:
                    response = requests.post(f"{BACKEND_URL}/briefing/", json={
                        "symbols": symbols,
                        "query": query
                    })
                    data = response.json()

                st.subheader("📋 Market Summary")
                st.success(data.get("summary", "⚠️ No summary returned."))

            except Exception as e:
                st.error(f"⚠️ Failed to connect: {e}")

# --- VOICE MODE ---
else:
    file = st.file_uploader("🎤 Upload your question as a WAV file", type=["wav"])
    if file and st.button("Submit Voice"):
        with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp:
            tmp.write(file.read())
            tmp_path = tmp.name

        with st.spinner("Processing voice..."):
            try:
                if DEMO_MODE:
                    data = {
                        "query": "What is our Asia tech exposure?",
                        "summary": "🧪 [Demo] Asia tech exposure is 22%. TSMC earnings were strong, Samsung weaker. Consider diversifying."
                    }
                else:
                    response = requests.post(f"{BACKEND_URL}/voice/", files={"file": open(tmp_path, "rb")})
                    data = response.json()

                st.subheader("🗣️ Transcribed Query")
                st.info(data.get("query", "N/A"))

                st.subheader("📋 Market Summary")
                st.success(data.get("summary", "⚠️ No summary returned."))

                st.subheader("🔊 Audio Output")
                st.audio("output.wav")

            except Exception as e:
                st.error(f"⚠️ Voice processing failed: {e}")
