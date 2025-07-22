import streamlit as st
from config import GOOGLE_API_KEY
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory
from tools.calculator import calculator_tool
import re

# Setup Gemini Chat Model
llm = ChatGoogleGenerativeAI(
    google_api_key=GOOGLE_API_KEY,
    model="gemini-2.0-flash",
    temperature=0.7
)

def get_session_history(session_id: str):
    return ChatMessageHistory()

conversation = RunnableWithMessageHistory(
    llm,
    get_session_history=get_session_history,
)

st.title("🧠 Mini Agentic Chatbot")

if 'history' not in st.session_state:
    st.session_state['history'] = []
if 'session_id' not in st.session_state:
    st.session_state['session_id'] = 'default'

user_input = st.text_input("You:", "", key="input")

if st.button("Send") or user_input:
    if user_input.lower().startswith("calculate "):
        expression = user_input[len("calculate "):]
        result = calculator_tool(expression)
        st.session_state['history'].append(("You", user_input))
        st.session_state['history'].append(("Tool", result))
    else:
        reply = conversation.invoke({"input": user_input}, config={"configurable": {"session_id": st.session_state['session_id']}}).content
        st.session_state['history'].append(("You", user_input))
        st.session_state['history'].append(("Bot", reply))
    st.rerun()

for speaker, text in st.session_state['history']:
    if speaker == "You":
        st.markdown(f"**You:** {text}")
    elif speaker == "Bot":
        st.markdown(f"**Bot:** {text}")
    else:
        st.markdown(f"**{speaker}:** {text}") 