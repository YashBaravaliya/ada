import os
import streamlit as st
import google.generativeai as genai

genai.configure(api_key="AIzaSyDMnQYqb8yzAlZTf9r0LlkA21xM91US3k0")
model = genai.GenerativeModel('gemini-pro')

st.set_page_config(
    page_icon="logo.ico" 
)

if "chat" not in st.session_state:
    st.session_state.chat = model.start_chat(history=[])

st.title("Ada")
st.subheader("Your AI assistant, always adapting.")

def role_to_streamlit(role):
    if role == "model":
        return "assistant"
    else:
        return role
    
for message in st.session_state.chat.history:
    with st.chat_message(role_to_streamlit(message.role)):
        st.markdown(message.parts[0].text)


if prompt := st.chat_input("I Possess a well of knowledge. What would you like to now?"):
    st.chat_message("user").markdown(prompt)
    response = st.session_state.chat.send_message(prompt)
    with st.chat_message("assistant"):
        st.markdown(response.text)
    