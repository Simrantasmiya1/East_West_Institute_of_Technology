import streamlit as st
from agent.agent_controller import process_query

st.set_page_config(
    page_title="Interactive Campus Info AI Agent",
    layout="centered"
)

st.title("🎓 Interactive Campus Info AI Agent")

st.write(
    "Welcome! I am your campus information assistant. "
    "I will help you with college-related queries."
)

user_query = st.text_input("Ask your campus question here:")

if user_query:
    response = process_query(user_query)
    st.markdown("### 🤖 Agent Response")
    st.write(response)

