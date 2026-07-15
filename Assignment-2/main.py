import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-flash-latest")
st.title("AI Multiverse")
st.sidebar.title("App Settings")
personality = st.sidebar.selectbox(
    "Choose AI Personality",
    [
        "Ironman",
        "A Ronaldo fan",
        "A 1920s Mafia Boss",
        "A Fitness Coach",
        "An Expert Hacker"
    ]
)
intensity = st.sidebar.slider(
    "Intensity Level",
    min_value=1,
    max_value=10,
    value=5
)
if personality == "Ironman":
    bot_avatar = "🦾"
elif personality == "A Ronaldo fan":
    bot_avatar = "⚽"
elif personality == "A 1920s Mafia Boss":
    bot_avatar = "🕴️"
elif personality == "A Fitness Coach":
    bot_avatar = "💪"
elif personality == "An Expert Hacker":
    bot_avatar = "💻"
else:
    bot_avatar = "🤖"

user_message = st.text_input("Enter your message")
if st.button("SEND"):

    if user_message.strip() == "":
        st.warning("Please enter a message.")
    else:

        ai_instructions = (
            f"You are {personality}. "
            f"Act with intensity {intensity}/10. "
            f"Reply to: {user_message}"
        )
        response = model.generate_content(ai_instructions)

        with st.chat_message("user"):
            st.write(user_message)

        with st.chat_message("assistant", avatar=bot_avatar):
            st.write(response.text)