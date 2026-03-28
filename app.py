import streamlit as st
import pandas as pd
import plotly.express as px
import os
from agent.agent_controller import agent_response

# 🎤 Voice support (safe import)
try:
    from streamlit_mic_recorder import mic_recorder
    VOICE_AVAILABLE = True
except:
    VOICE_AVAILABLE = False

# =====================================================
# ⚙️ PAGE CONFIG
# =====================================================

st.set_page_config(
    page_title="AI Campus Intelligence System",
    layout="wide"
)

# =====================================================
# 🎨 UI STYLE
# =====================================================

st.markdown("""
<style>
.big-title {
    font-size:40px !important;
    font-weight:700;
    color:#4CAF50;
    text-align:center;
}
.card {
    padding:20px;
    border-radius:15px;
    background-color:#f5f5f5;
    box-shadow: 0px 4px 10px rgba(0,0,0,0.1);
}
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="big-title">🎓 AI Campus Career Intelligence Dashboard</div>', unsafe_allow_html=True)

st.write("Ask me anything about departments, career guidance, or branch recommendations.")

# =====================================================
# 🔥 MEMORY INITIALIZATION
# =====================================================

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

if "interest" not in st.session_state:
    st.session_state.interest = None

if "branch_scores" not in st.session_state:
    st.session_state.branch_scores = {}

# =====================================================
# 🔹 INPUT SECTION (FIXED)
# =====================================================

text_query = st.text_input("💬 Ask your question:")

voice_query = None

# 🎤 Voice Input
if VOICE_AVAILABLE:
    st.subheader("🎤 Voice Input")
    audio = mic_recorder(start_prompt="Start Recording", stop_prompt="Stop")

    if audio:
        st.success("Voice recorded (Demo mode)")
        voice_query = "I like coding"   # demo simulation

# 👉 PRIORITY: TEXT > VOICE
user_query = None

if text_query:
    user_query = text_query
elif voice_query:
    user_query = voice_query

# =====================================================
# 🤖 PROCESS INPUT (NO DUPLICATE FIX)
# =====================================================

if user_query and (
    len(st.session_state.chat_history) == 0 or
    st.session_state.chat_history[-1][1] != user_query
):
    with st.spinner("🤖 AI is thinking..."):
        response = agent_response(user_query, st.session_state)

    st.session_state.chat_history.append(("You", user_query))
    st.session_state.chat_history.append(("Agent", response))

# =====================================================
# 🔹 LAYOUT
# =====================================================

col1, col2 = st.columns([2, 1])

# ------------------------------
# 💬 CHAT SECTION
# ------------------------------

with col1:
    st.subheader("💬 Conversation")

    st.markdown('<div class="card">', unsafe_allow_html=True)

    for speaker, message in st.session_state.chat_history:
        if speaker == "You":
            st.markdown(f"👤 **You:** {message}")
        else:
            st.markdown(f"🤖 **Agent:** {message}")

    st.markdown('</div>', unsafe_allow_html=True)

# ------------------------------
# 📊 DASHBOARD
# ------------------------------

with col2:
    st.subheader("📊 Branch Suitability Dashboard")

    scores = st.session_state.get("branch_scores", {})

    if scores:
        df = pd.DataFrame({
            "Branch": list(scores.keys()),
            "Score": list(scores.values())
        })

        fig = px.bar(
            df,
            x="Branch",
            y="Score",
            color="Score",
            color_continuous_scale="viridis",
            title="AI Suitability Ranking"
        )

        st.plotly_chart(fig, use_container_width=True)

        st.metric(
            label="🎯 AI Confidence Level",
            value=f"{max(scores.values())}%"
        )

    else:
        st.info("Ask about coding, AI, or machines to see AI analysis dashboard.")

# =====================================================
# 📄 PDF DOWNLOAD
# =====================================================

if os.path.exists("AI_Career_Report.pdf"):
    with open("AI_Career_Report.pdf", "rb") as file:
        st.download_button(
            label="📄 Download AI Career Report",
            data=file,
            file_name="AI_Career_Report.pdf",
            mime="application/pdf"
        )