# 🧠 mini-agentic-chatbot

A lightweight, modular chatbot built in Python using Gemini (Google Generative AI) and LangChain. Supports terminal, web API (Flask), and Streamlit UI. Includes memory and tools (like calculator). Ready for deployment and extensible with more tools.

## 🚀 Features
- Short-term memory (chat history)
- CLI, Web API, and Streamlit UI
- Modular file structure
- Tool support (calculator included)
- Gemini (Google Generative AI) integration

## 🛠 Tech Stack
- Python
- Gemini API (Google Generative AI)
- dotenv
- LangChain
- Flask (web API)
- Streamlit (web UI)

## 🔧 Setup

1. **Clone the repo:**
   ```bash
   git clone https://github.com/theShrijith/mini-agentic-chatbot.git
   cd mini-agentic-chatbot
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Create a `.env` file:**
   ```
   GOOGLE_API_KEY=your_gemini_api_key_here
   ```
   Replace `your_gemini_api_key_here` with your Gemini API key from [Google AI Studio](https://aistudio.google.com/app/apikey) or Google Cloud Console.

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
python -m streamlit run interface.py
```

## 🌍 Deployment

### Render
- Create a new Web Service, connect your repo.
- Set build command: `pip install -r requirements.txt`
- Set start command: `python app.py` (for API) or `python -m streamlit run interface.py` (for UI)
- Add your `GOOGLE_API_KEY` in the environment variables.

### Replit
- Import the repo.
- Add `.env` with your Gemini key.
- Run `python app.py` or `python -m streamlit run interface.py`.

## 📦 .env Example
```
GOOGLE_API_KEY=your_gemini_api_key_here
```

## 🛠️ Troubleshooting & Common Errors

- **404 Not Found on `/`**: The Flask API only serves `/chat` as a POST endpoint. Use tools like Postman or PowerShell to POST to `/chat`.
- **API key expired or invalid**: If you see `API key expired` or `API_KEY_INVALID`, generate a new key from [Google AI Studio](https://aistudio.google.com/app/apikey) and update your `.env`.
- **Quota exceeded / 429 errors**: You have hit the free tier or per-minute quota. Wait and try again later, or upgrade your plan.
- **Model not found (404)**: Make sure you are using the correct model name (e.g., `gemini-2.0-flash`).
- **Streamlit not recognized**: Use `python -m streamlit run interface.py` if `streamlit` is not in your PATH.

## 🧩 Extending
- Add more tools in the `tools/` directory and import them in your main logic.
- The codebase is modular and ready for further agentic or retrieval-augmented features.

