# 🤖 AI Chatbot using Ollama (Local LLM)

## 📌 Overview
This project is an AI-powered chatbot built using Python and Flask, integrated with a local Large Language Model (LLM) using Ollama. Unlike cloud-based APIs, this chatbot runs completely on a local environment, enabling cost-free and privacy-focused AI interactions.

The system accepts user input through a REST API, processes it using a locally hosted LLM (phi3 model), and returns a contextual response.

---

## 🚀 Features
- 🧠 Local LLM integration using Ollama (phi3 model)
- ⚡ Real-time chatbot responses
- 🔗 REST API built with Flask
- 📦 JSON-based request and response handling
- 💻 No external API dependency (runs offline)
- 🧪 Tested using Postman

---

## 🛠️ Tech Stack
- **Language:** Python  
- **Backend:** Flask  
- **LLM Engine:** Ollama (phi3 model)  
- **Tools:** Postman, Git, GitHub  

---

## 🧩 System Architecture

User Input → Flask API → Ollama (Local LLM) → Response → JSON Output

---

## 📂 Project Structure
ai-chatbot-ollama/
│── app.py # Main Flask application
│── requirements.txt # Dependencies
│── README.md # Project documentation


---

## ⚙️ Setup Instructions

### 1️⃣ Install Ollama
Download and install Ollama from:
https://ollama.com

---

### 2️⃣ Run LLM Model
```
ollama run phi3:mini
```
### 3️⃣ Install Dependencies
pip install -r requirements.txt
```
```
### 4️⃣ Run Flask App
python app.py
```
```
### 5️⃣ Test API (Postman)
Method: POST
URL:
http://127.0.0.1:5000/chat
Body (JSON):
{
  "message": "Explain Artificial Intelligence"
}
```

```
### 📥 Sample Input
{
  "message": "What is Machine Learning?"
}
```
```
### 📤 Sample Output
{
  "input": "What is Machine Learning?",
  "response": "Machine Learning is a subset of Artificial Intelligence that allows systems to learn from data and improve their performance without being explicitly programmed..."

}
```

