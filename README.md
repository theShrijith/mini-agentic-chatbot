# 🧠 mini-agentic-chatbot

A lightweight, modular chatbot built in Python using OpenAI API and LangChain. Supports terminal, web API (Flask), and Streamlit UI. Includes memory and tools (like calculator).

## 🚀 Features
- Short-term memory (chat history)
- CLI, Web API, and Streamlit UI
- Modular file structure
- Tool support (calculator included)

## 🛠 Tech Stack
- Python
- OpenAI API (GPT-3.5 / GPT-4)
- dotenv
- LangChain
- Flask (web API)
- Streamlit (web UI)

## 🔧 Setup

1. **Clone the repo:**
   ```bash
   git clone https://github.com/yourusername/mini-agentic-chatbot.git
   cd mini-agentic-chatbot
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Create a `.env` file:**
   ```
   OPENAI_API_KEY=your_openai_key_here
   ```
   Replace `your_openai_key_here` with your OpenAI API key.

## 🖥️ Usage

### Terminal (CLI)
```bash
python main.py
```

### Web API (Flask)
```bash
python app.py
```
POST to `http://localhost:5000/chat` with JSON: `{ "input": "your message" }`

### Streamlit UI
```bash
streamlit run interface.py
```

## 🌍 Deployment

### Render
- Create a new Web Service, connect your repo.
- Set build command: `pip install -r requirements.txt`
- Set start command: `python app.py` (for API) or `streamlit run interface.py` (for UI)
- Add your `OPENAI_API_KEY` in the environment variables.

### Replit
- Import the repo.
- Add `.env` with your OpenAI key.
- Run `python app.py` or `streamlit run interface.py`.

## 📦 .env Example
```
OPENAI_API_KEY=your_openai_key_here
```

---
✅ Beginner-friendly, modular, and deployable. Works in Cursor IDE. 