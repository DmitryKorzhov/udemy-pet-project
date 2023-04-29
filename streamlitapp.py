import streamlit as st
from streamlit_chat import message

st.set_page_config(
    page_title="Streamlit Chat - Demo",
    page_icon=":robot:"
)

st.header("Streamlit Chat - Demo")

for message_ in message_history:
    message(message_)   # display all the previous message

placeholder = st.empty()  # placeholder for latest message
input_ = st.text_input("you:")
message_history.append(input_)

with placeholder.container():
    message(message_history[-1]) # display the latest message
