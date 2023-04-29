import openai
import streamlit as st
from streamlit_chat import message



openai.api_key=st.secrets["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"]

def generate_response(prompt):
    completions = openai.Completion.create (
        engine="text-davinci-003",
        prompt=prompt,
        temperature=0.9,
        max_tokens=150,
        top_p=1,
        frequency_penalty=0.0,
        presence_penalty=0.6,
        stop=[" Human:", " AI:"]
    )

    message = completions.choices[0].text
    return message

st.title('Lamis ChatBot  🤖 🤖')


if 'generated' not in st.session_state:
    st.session_state['generated'] = []

if 'past' not in st.session_state:
    st.session_state['past'] = []


def get_text():
    #input_text = st.text_input("Human [enter your message here]: "," Hello Mr AI how was your day today? ", key="input")
    input_text= st.text_input('Human [enter your message here]:', '')
    return input_text 


user_input = get_text()



if user_input:
    output = generate_response(user_input)
    st.session_state.past.append(user_input)
    st.session_state.generated.append(output)
    


if st.session_state['generated']:

    for i in range(len(st.session_state['generated'])-1, -1, -1):
        message(st.session_state["generated"][i], key=str(i))
        message(st.session_state['past'][i], is_user=True, key=str(i) + '_user')
