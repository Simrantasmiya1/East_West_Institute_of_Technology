import streamlit as st

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

# Chat input
user_query = st.text_input("Ask your campus question here:")

# Temporary response (Week 1 placeholder)
if user_query:
    st.markdown("### 🤖 Agent Response")
    st.write(
        "I am getting ready 🚀. "
        "In the next week, I will answer questions about departments, facilities, rules, and more."
    )