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

if __name__ == "__main__":
    print("🧠 Mini Agentic Chatbot w/ Gemini (type 'exit' to quit)")
    session_id = "default"
    while True:
        user_input = input("You: ")
        if user_input.lower() in ['exit', 'quit']:
            break
        if user_input.lower().startswith("calculate "):
            expression = user_input[len("calculate "):]
            result = calculator_tool(expression)
            print("Tool:", result)
            continue
        reply = conversation.invoke({"input": user_input}, config={"configurable": {"session_id": session_id}}).content
        print("Bot:", reply)