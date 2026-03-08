import streamlit as st
import pandas as pd
import plotly.express as px
import os
from agent.agent_controller import agent_response

st.set_page_config(
    page_title="AI Campus Intelligence System",
    layout="wide"
)

st.title("🎓 AI Campus Career Intelligence Dashboard")

st.write(
    "Ask me anything about departments, career guidance, or branch recommendations."
)

# ==============================
# 🔥 MEMORY INITIALIZATION
# ==============================

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

if "interest" not in st.session_state:
    st.session_state.interest = None

if "branch_scores" not in st.session_state:
    st.session_state.branch_scores = {}

# ==============================
# 🔹 INPUT
# ==============================

user_query = st.text_input("💬 Ask your question:")

if user_query:
    response = agent_response(user_query, st.session_state)

    st.session_state.chat_history.append(("You", user_query))
    st.session_state.chat_history.append(("Agent", response))

# ==============================
# 🔹 LAYOUT
# ==============================

col1, col2 = st.columns([2, 1])

# ------------------------------
# Conversation Section
# ------------------------------

with col1:
    st.subheader("💬 Conversation")

    for speaker, message in st.session_state.chat_history:
        if speaker == "You":
            st.markdown(f"👤 **You:** {message}")
        else:
            st.markdown(f"🤖 **Agent:** {message}")

# ------------------------------
# Dashboard Section
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

# ==============================
# 📄 PDF DOWNLOAD
# ==============================

if os.path.exists("AI_Career_Report.pdf"):
    with open("AI_Career_Report.pdf", "rb") as file:
        st.download_button(
            label="📄 Download AI Career Report",
            data=file,
            file_name="AI_Career_Report.pdf",
            mime="application/pdf"
        )
