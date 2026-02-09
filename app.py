import streamlit as st
from agent.agent_controller import agent_response

# Page configuration
st.set_page_config(
    page_title="Interactive Campus Info AI Agent",
    layout="centered"
)

# App title
st.title("🎓 Interactive Campus Info AI Agent")

st.write(
    "Welcome! I am your campus information assistant. "
    "I will help you with college-related queries."
)

# User input
user_query = st.text_input("Ask your campus question here:")

# Agent response
if user_query:
    st.markdown("### 🤖 Agent Response")
    response = agent_response(user_query)
    st.write(response)
