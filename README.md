# Plantify-ChatBot 🌾

Plantify-ChatBot is an AI-powered farming assistant built using Streamlit and the OpenAI API.  
It answers agriculture-related questions in English and strictly restricts responses to farming-focused topics.

---

## 🚀 Live Demo

🔗 https://plantify-chatbot-anhzrhvjbmw8wbyn6ridhd.streamlit.app/

---

## ✨ Features

- 🌱 Agriculture & farming domain-focused chatbot  
- 🚫 Politely rejects non-farming queries  
- 🌍 English-only responses  
- 💬 Interactive chat-style interface  
- 🔐 Secure API key handling using Streamlit Secrets  
- ☁️ Deployed on Streamlit Cloud  

---

## 🛠 Tech Stack

- Python  
- Streamlit  
- OpenAI API (`gpt-4o-mini`)  
- dotenv (for local development)

---

## 📂 Project Structure
```bash
Plantify-ChatBot/
│
├── app.py  
├── requirements.txt  
├── .gitignore  
├── .env.example  
└── README.md  
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/Plantify-ChatBot.git
cd Plantify-ChatBot
```

### 2️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 3️⃣ Configure Environment Variables (Local)
Create a .env file in the root directory:
---
OPENAI_API_KEY=your_openai_api_key_here
---

### ▶️ Run the Application
```bash
streamlit run app.py
```

### ☁️ Deployment (Streamlit Cloud)
Go to:

Manage App → Secrets

Add the following in TOML format:
```bash
OPENAI_API_KEY = "your_openai_api_key_here"
```
Then reboot the application.

### 🎯 Assistant Behavior

The chatbot:
- Responds only to farming and agriculture-related queries
- Rejects out-of-domain questions politely
- Responds strictly in English
- Greets users with a custom introduction

### 👨‍💻 Author
Sabhya Rajvanshi
B.Tech CSE (AI/ML)
AI Developer

