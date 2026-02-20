Plantify-ChatBot 🌾

Plantify-ChatBot is an AI-powered farming assistant built using Streamlit and the OpenAI API.
It answers agriculture-related questions in English and restricts responses to farming-focused topics only.

🚀 Live Demo

Add your Streamlit deployment link here:

https://your-app-link.streamlit.app
✨ Features

🌱 Agriculture & farming domain-focused chatbot

🚫 Politely rejects non-farming queries

🌍 English-only responses

💬 Chat-style user interface

🔐 Secure API key handling using Streamlit Secrets

☁️ Deployed on Streamlit Cloud

🛠 Tech Stack

Python

Streamlit

OpenAI API (gpt-4o-mini)

dotenv (for local environment setup)

📂 Project Structure
Plantify-ChatBot/
│
├── app.py
├── requirements.txt
├── .gitignore
├── .env.example
└── README.md
⚙️ Setup Instructions
1️⃣ Clone Repository
git clone https://github.com/your-username/Plantify-ChatBot.git
cd Plantify-ChatBot
2️⃣ Install Dependencies
pip install -r requirements.txt
3️⃣ Add Environment Variable (Local)

Create a .env file:

OPENAI_API_KEY=your_openai_api_key_here
4️⃣ Run Application
streamlit run app.py
☁️ Deployment (Streamlit Cloud)

Go to:

Manage App → Secrets

Add:

OPENAI_API_KEY = "your_openai_api_key_here"

Then reboot the app.

👨‍💻 Author

Sabhya Rajvanshi
B.Tech CSE (AI/ML)
AI Developer
