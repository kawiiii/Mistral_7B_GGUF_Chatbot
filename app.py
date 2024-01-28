import streamlit as st
import requests

USER_AVATAR = 'images/man.png'
MODEL_AVATAR = 'images/mistral.png'

def write_history(text):
    with open('chathistory.txt', 'a') as f:
        f.write(text)
        f.write('\n')

def display_message(role, content, avatar):
    with st.chat_message(role, avatar=avatar):
        st.markdown(content)

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
        display_message(
            message["role"],
            message["content"],
            USER_AVATAR if message["role"] == "user" else MODEL_AVATAR
        )
def chat_interaction():
    if user_input := st.chat_input("What can you do for me?"):
        st.session_state.messages.append({"role": "user", "content": user_input})
        display_message("user", f"user: {user_input}", USER_AVATAR)
        usertext = f"user: {user_input}"
        write_history(usertext)

        with st.chat_message("assistant", avatar=MODEL_AVATAR):
            message_placeholder = st.empty()

            url = f'http://127.0.0.1:8000/mistral?query={user_input}'
            response_stream = requests.get(url, stream=True)

            asstext = ""
            for chunk in response_stream.iter_content(chunk_size=1024):
                try:
                    if chunk:
                        asstext += chunk.decode('utf-8')
                        message_placeholder.markdown(asstext, unsafe_allow_html=True)
                except requests.exceptions.ChunkedEncodingError as e:
                    print(f"Error in handling chunked response: {e}")

            
            st.session_state.messages.append({"role": "assistant", "content": asstext})
            write_history(asstext)
            

if __name__ == "__main__":
    setup_app()
    chat_interaction()
