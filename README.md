# 🚀 Lumos — AI Chat Dashboard (Gemini Powered)

Lumos is a modern AI chat dashboard built using **Flask** and powered by **Google Gemini API**. It provides a clean UI for real-time conversations, session management, and live usage stats.

---

## ✨ Features

* 💬 Real-time AI chat interface
* ⚡ Powered by **Gemini (Google AI)**
* 🧠 Session-based conversation memory
* 📊 Live stats (messages, sessions, latency)
* 🔄 Clear chat & history support
* 🎨 Clean and responsive UI

---

## 🛠️ Tech Stack

* **Frontend:** HTML, CSS, JavaScript
* **Backend:** Flask (Python)
* **AI Model:** Gemini (google-genai SDK)

---

## 📦 Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/lumos-ai-dashboard.git
cd lumos-ai-dashboard
```

---

### 2. Create virtual environment (recommended)

```bash
python -m venv venv
venv\Scripts\activate   # Windows
# source venv/bin/activate   # Mac/Linux
```

---

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Setup Environment Variables

Create a `.env` file in the root directory:

```env
GEMINI_API_KEY=your_api_key_here
```

---

### 5. Run the application

```bash
python app.py
```

Now open:

```
http://127.0.0.1:5000
```

---

## 🔑 Getting Gemini API Key

1. Go to: https://aistudio.google.com/app/apikey
2. Sign in with Google
3. Click **Create API Key**
4. Copy and paste into `.env`

---

## 📁 Project Structure

```
lumos-ai-dashboard/
│── app.py
│── requirements.txt
│── .env
│── templates/
│   └── index.html
│── static/
│   ├── css/
│   └── js/
```

---

## ⚙️ API Endpoints

### Chat

```
POST /api/chat
```

### Get Stats

```
GET /api/stats
```

### Get History

```
GET /api/history/<session_id>
```

### Clear Session

```
POST /api/clear/<session_id>
```

---

## 📊 Example Request

```json
{
  "message": "Hello AI!",
  "session_id": "default"
}
```

---

## 🚀 Future Improvements

* 🔁 Multi-model support (Gemini + GPT + Claude)
* 🌐 Deployment (Render / Vercel / AWS)
* 🎙️ Voice input/output
* 📱 Mobile responsive UI
* ⚡ Streaming responses

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repo
2. Create a new branch
3. Make your changes
4. Submit a pull request

---

## 📜 License

This project is open-source and available under the **MIT License**.

---

## 👨‍💻 Author

Developed by **Your Name**

---

⭐ If you like this project, give it a star!
