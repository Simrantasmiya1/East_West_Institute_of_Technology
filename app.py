import streamlit as st
from agent.agent_controller import agent_response

# Page configuration
st.set_page_config(
    page_title="Interactive Campus Info AI Agent",
    page_icon="🎓",
    layout="centered"
)

# Header
st.markdown("## 🎓 Interactive Campus Info AI Agent")
st.write(
    "Welcome! I am your campus information assistant. "
    "Ask me anything related to your college."
)

st.divider()

# Input box
user_query = st.text_input(
    "💬 Ask your campus question here:",
    placeholder="e.g. What departments are available?"
)

# Response section
if user_query:
    with st.spinner("Thinking... 🤖"):
        response = agent_response(user_query)

    st.markdown("### 🤖 Agent Response")
    st.success(response)

# Footer
st.divider()
st.caption("🚀 Built as part of Agentic AI Hackathon | Week-5")
