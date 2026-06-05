# Lumos — AI Chat Dashboard

A beautiful AI chatbot dashboard powered by Claude and Flask.

## Setup

1. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

2. **Set your API key**
   ```bash
   export ANTHROPIC_API_KEY=your_api_key_here
   ```

3. **Run the server**
   ```bash
   python app.py
   ```

4. **Open your browser**
   Navigate to `http://localhost:5000`

## Features

- 💬 Multi-turn conversations with full context
- 🔄 Model switching (Haiku for speed, Sonnet for depth)
- 📊 Live stats — messages, tokens, sessions, uptime
- ⚡ Latency tracking per response
- 🗂 Multiple sessions via "New conversation"
- 🌙 Dark theme with smooth animations

## Project Structure

```
chatbot/
├── app.py              # Flask backend
├── requirements.txt
└── templates/
    └── index.html      # Dashboard UI
```

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Dashboard UI |
| POST | `/api/chat` | Send a message |
| GET | `/api/stats` | Live statistics |
| GET | `/api/history/<id>` | Session history |
| POST | `/api/clear/<id>` | Clear a session |
