from flask import Flask, request, jsonify
from config import GOOGLE_API_KEY
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory
from tools.calculator import calculator_tool
import re

app = Flask(__name__)

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

@app.route('/chat', methods=['POST'])
def chat():
    try:
        data = request.get_json()
        user_input = data.get('input', '')
        session_id = data.get('session_id', 'default')
        if user_input.lower().startswith("calculate "):
            expression = user_input[len("calculate "):]
            result = calculator_tool(expression)
            return jsonify({"tool": result})
        reply = conversation.invoke({"input": user_input}, config={"configurable": {"session_id": session_id}}).content
        return jsonify({"bot": reply})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000) 