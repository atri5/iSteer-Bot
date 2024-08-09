import streamlit as st
from Chatbot import Chatbot

chatter = Chatbot()

# Initialize session state to store the conversation history
if 'conversation' not in st.session_state:
    st.session_state.conversation = []

if 'input_text' not in st.session_state:
    st.session_state.input_text = ""

def send_message():
    user_input = st.session_state.input_text
    if user_input:
        # Append user input to conversation
        st.session_state.conversation.append(f"You: {user_input}")
        
        # Get the chatbot response
        response = chatter.chat(user_input)
        st.session_state.conversation.append(f"Chatbot: {response}")
        
        # Clear the input box after sending
        st.session_state.input_text = ""

# Streamlit app layout
st.title("iSteer Installation Assistant")

# Display the conversation history
for message in st.session_state.conversation:
    st.write(message)

# Text input for user prompt with submit button
st.text_input('You: ', key='input_text')
st.button('Send', on_click=send_message)

# Allow clearing the conversation
if st.button("Clear Chat"):
    st.session_state.conversation = []
