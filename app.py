import streamlit as st
import google.generativeai as genai

# Gemini API key
genai.configure(api_key=st.secrets["api_key"])

# Load the model
model = genai.GenerativeModel("models/gemini-1.5-flash")

# Streamlit UI
st.set_page_config(page_title="Gemini Chatbot 💬")
st.title("🤖 Gemini Chatbot")

# Store chat history in session state
if "chat" not in st.session_state:
    st.session_state.chat = model.start_chat(history=[])

if "messages" not in st.session_state:
    st.session_state.messages = []

# Chat display
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# User input
prompt = st.chat_input("Type your message here...")

if prompt:
    # Display user message
    st.chat_message("user").markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    try:
        # Send to Gemini
        response = st.session_state.chat.send_message(prompt)
        reply = response.text

        # Display Gemini reply
        st.chat_message("ai").markdown(reply)
        st.session_state.messages.append({"role": "ai", "content": reply})

    except Exception as e:
        st.error(f"❌ Error: {e}")
