from time import sleep
import requests
import streamlit as st
import json

# AVATARS
av_us = 'images/man.png'
av_ass = 'images/mistral.png'

# FUNCTION TO LOG ALL CHAT MESSAGES INTO chathistory.txt
def write_history(text):
    with open('chathistory.txt', 'a') as f:
        f.write(text)
        f.write('\n')

# Function to display chat messages with avatars
def display_message(role, content, avatar):
    with st.chat_message(role, avatar=avatar):
        st.markdown(content)

# Function to get assistant response
def get_assistant_response(user_input):
    api_response = requests.get(f'http://127.0.0.1:8000/mistral?question={user_input}')

    # formatted_response = api_response.content.decode("utf-8")[1:-1]
    formatted_response = api_response.json()["result"]
    return formatted_response

# Streamlit App Setup

def setup_app():
    st.title("🤖 ChatBot")
    st.subheader("Using Mistral 7-B")
    repo = "model/mistral-7b-v0.1.Q4_K_M.gguf"

    # Set a default model
    if "hf_model" not in st.session_state:
        st.session_state["hf_model"] = repo

    # Initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display chat messages from history on app rerun
    for message in st.session_state.messages:
        display_message(message["role"], message["content"], av_us if message["role"] == "user" else av_ass)
    
# Streamlit App Interaction
def chat_interaction():
    if user_input := st.chat_input("What can you do for me?"):
        st.session_state.messages.append({"role": "user", "content": user_input})
        display_message("user", f"user: {user_input}", av_us)
        usertext = f"user: {user_input}"
        write_history(usertext)

        with st.chat_message("assistant", avatar=av_ass):
            message_placeholder = st.empty()
            full_response = get_assistant_response(user_input)
            message_placeholder.markdown(full_response)
            asstext = f"assistant: {full_response}"
            write_history(asstext)
            st.session_state.messages.append({"role": "assistant", "content": full_response})

if __name__ == "__main__":
    setup_app()
    chat_interaction()


