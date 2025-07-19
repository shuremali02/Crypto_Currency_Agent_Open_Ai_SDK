import streamlit as st
from agents import Runner
from agent import Crypto_Agent
from connection import config
import asyncio

st.set_page_config(page_title="Crypto Market Conversational Chatbot")
st.title("🪙 Crypto Market Conversational Chatbot")

# Chat history maintain kro
if "messages" not in st.session_state:
    st.session_state.messages = []

# Show past messages with labels
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# User input
user_input = st.chat_input("Ask me anything about the crypto market...")

if user_input:
    # Show user input in chat
    st.chat_message("user").markdown(user_input)
    st.session_state.messages.append({"role": "user", "content": user_input})

    # Run the agent asynchronously
    async def get_response(input_text):
        result = await Runner.run(Crypto_Agent, input=input_text, run_config=config)
        return result.final_output

    # Run and get the output
    response = asyncio.run(get_response(user_input))

    # Show response in chat
    st.chat_message("assistant").markdown(response)
    st.session_state.messages.append({"role": "assistant", "content": response})
