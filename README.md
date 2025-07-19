# 🤖 OpenAI Chatbot with Streamlit
DEMO:-https://ai-agent-cvtxvnenvdkbnta3vjfpsv.streamlit.app/
This is a simple chatbot web app built with [Streamlit](https://ai-agent-cvtxvnenvdkbnta3vjfpsv.streamlit.app/) and powered by an API (like OpenAI or Gemini). It uses a local virtual environment and securely stores the API key using `secrets.toml`.

---

## 🚀 Features

- Conversational chatbot UI
- API key stored securely using Streamlit's `secrets.toml`
- Runs locally in your browser
- Clean, easy-to-edit Python code

---

## 📁 Project Structure
openaichatbot/
├── app.py
├── venv/
├── .streamlit/
│ └── secrets.toml
└── README.md


---

## 🛠️ Setup Instructions

### 1. Create & Activate Virtual Environment

```bash
# Open Command Prompt and run:
cd C:\Users\shiva\OneDrive\Desktop\openaichatbot
python -m venv venv
venv\Scripts\activate

pip install streamlit
pip install google-generativeai  # Or openai, if you're using OpenAI

openaichatbot/.streamlit/secrets.toml
streamlit run app.py

