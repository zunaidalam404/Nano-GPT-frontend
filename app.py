import streamlit as st
import requests

# Backend API
API_URL = "https://nano-gpt-0111.onrender.com/chat"

# Page Configuration
st.set_page_config(
    page_title="My Custom GPT",
    page_icon="🤖",
    layout="centered"
)

# Title
st.title("🤖 My Custom GPT")
st.caption("Powered by My Own Trained GPT Model")

# Chat History
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display Previous Messages
for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User Input
prompt = st.chat_input("Ask me anything...")

if prompt:

    # Display User Message
    st.session_state.messages.append({
        "role": "user",
        "content": prompt
    })

    with st.chat_message("user"):
        st.markdown(prompt)

    # Generate AI Response
    with st.chat_message("assistant"):

        with st.spinner("Thinking..."):

            try:
                response = requests.post(
                    API_URL,
                    json={"message": prompt},
                    timeout=180
                )

                response.raise_for_status()

                answer = response.json()["answer"]

                st.markdown(answer)

                st.session_state.messages.append({
                    "role": "assistant",
                    "content": answer
                })

            except requests.exceptions.RequestException as e:

                st.error(f"API Error: {e}")