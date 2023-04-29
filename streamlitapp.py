import streamlit as st
from streamlit_chat import message

# Add CSS styles
st.markdown("""
<style>
    .input-field {
        font-size: 18px;
        padding: 10px;
        border: 1px solid #ccc;
        border-radius: 4px;
    }
</style>
""", unsafe_allow_html=True)

# Chat logic function
def chat_logic(user_message):
    return "I don't know."

# User input field
st.markdown("### Ask the bot a question:")
user_message = st.text_input("", key="user_input", on_change=None, max_chars=None, type="default", help=None, placeholder="Type your question here...", className="input-field")

if user_message:
    message(user_message, is_user=True)  # User's message

    bot_response = chat_logic(user_message)  # Get the bot's response
    message(bot_response)  # Bot's response

