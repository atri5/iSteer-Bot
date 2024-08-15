import streamlit as st
from Chatbot import Chatbot



if 'input_text' not in st.session_state:
    st.session_state.input_text = ""

def send_pretty_message():
    user_input = st.chat_input("Ask a question")
    if user_input:
        with st.chat_message("User"):
            st.markdown(user_input)
        st.session_state.messages.append({"role": "User", "content": user_input})
    
        response = chatter.chat(user_input)
        with st.chat_message("Assistant"):
            st.write(response)
        st.session_state.messages.append({"role": "Assistant", "content": response})


# Streamlit app layout
st.title("iSteer Installation Assistant")

chatter = Chatbot()
ini_response = "Hello! I am here to assist you with any questions regarding Tibco EBX. I can answer specific installation questions while also assisting you in setting up Tibco on numerous platforms."

# Initialize session state to store the conversation history
if 'messages' not in st.session_state:
    st.session_state.messages = []
    st.session_state.messages.append({"role": "Assistant", "content" : ini_response})

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

send_pretty_message()
