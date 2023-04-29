import streamlit as st
from streamlit_chat import message

st.set_page_config(
    page_title="Streamlit Chat - Demo",
    page_icon=":robot:"
)

st.header("Streamlit Chat - Demo")

if 'generated' not in st.session_state:
    st.session_state['generated'] = []

if 'past' not in st.session_state:
    st.session_state['past'] = []

def display_conversation_history():
    if st.session_state['generated']:
        for i in range(len(st.session_state['generated'])-1, -1, -1):
            message(st.session_state["generated"][i], key=str(i))
            message(st.session_state['past'][i], is_user=True, key=str(i) + '_user')

def get_text():
    input_text = st.text_input("You: ", "Hello, how are you?", key="input")
    return input_text 

display_conversation_history()

user_input = get_text()

if st.button("Send"):
    output = "I don't know"
    st.session_state.past.append(user_input)
    st.session_state.generated.append(output)
    display_conversation_history()
