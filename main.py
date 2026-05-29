import streamlit as st
from agent_executor import AgentExecutor


# 🔹 Initialize Agent
agent = AgentExecutor()

st.set_page_config(page_title="Autonomous Job Agent", layout="wide")

st.title("🤖 Autonomous Job Application Agent")

# 🔹 Sidebar (Resume Input)
st.sidebar.header("📄 Resume Input")

resume_text = st.sidebar.text_area(
    "Paste your resume here:",
    height=300
)

# 🔹 Main Input
st.header("🔍 Job Query")

user_input = st.text_input("Enter your request:")

# 🔹 Run Button
if st.button("Run Agent"):
    if not user_input:
        st.warning("⚠️ Please enter a query")
    else:
        with st.spinner("🤖 Agent is working..."):
            response = agent.run(user_input, resume_text)

        st.success("✅ Done")
        st.subheader("📢 Result")
        st.write(response)