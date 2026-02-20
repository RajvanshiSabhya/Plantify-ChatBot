import os
import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

# Initialize OpenAI client
client = OpenAI(api_key=api_key)

# Page configuration
st.set_page_config(page_title="🌾 Farming AI Assistant")

st.title("🌾 Farming AI Assistant")
st.write("Ask farming and agriculture related questions only (English only).")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "system",
            "content": """You are a helpful AI assistant that only answers in english language
            related to farming and agriculture queries of the farmers. 
            If the question comes out of farming or agricultural domain then politely respond: 
            I can answer only to the farming based queries, sorry I won't be able to help you with that. 
            If the question is asked other than english language then respond saying 
            My apologies but I can only answer in english language.
            
            If you get hi or any similar message from it respond politely with Hi, I am Plantify your personal Farming Assitant.
            How can I help you today?"""
        },
    ]

# Display previous chat messages
for msg in st.session_state.messages[1:]:  # Skip system message
    if msg["role"] == "user":
        st.chat_message("user").write(msg["content"])
    else:
        st.chat_message("assistant").write(msg["content"])

# Chat input box
user_input = st.chat_input("Type your farming question here...")

if user_input:
    # Display user message
    st.chat_message("user").write(user_input)
    st.session_state.messages.append({"role": "user", "content": user_input})

    # Get AI response
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=st.session_state.messages
    )

    assistant_reply = response.choices[0].message.content

    # Display assistant message
    st.chat_message("assistant").write(assistant_reply)
    st.session_state.messages.append({"role": "assistant", "content": assistant_reply})