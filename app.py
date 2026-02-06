import streamlit as st
from agent.agent_controller import handle_query

st.set_page_config(
    page_title="Interactive Campus Info AI Agent",
    layout="centered"
)

st.title("🎓 Interactive Campus Info AI Agent")

st.write(
    "Welcome! I am your campus information assistant. "
    "Ask me about office timings and basic campus info."
)

user_query = st.text_input("Ask your campus question here:")

if user_query:
    st.markdown("### 🤖 Agent Response")
    response = handle_query(user_query)
    st.write(response)
