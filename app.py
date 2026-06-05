import os
import time
from datetime import datetime
from flask import Flask, request, jsonify, render_template

from google import genai

app = Flask(__name__)

# Gemini client
client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

chat_sessions = {}

stats = {
    "total_messages": 0,
    "total_tokens": 0,
    "sessions_created": 0,
    "start_time": time.time()
}


def get_or_create_session(session_id):
    if session_id not in chat_sessions:
        chat_sessions[session_id] = {
            "messages": [],
            "created_at": datetime.now().isoformat(),
            "message_count": 0
        }
        stats["sessions_created"] += 1

    return chat_sessions[session_id]


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api/chat", methods=["POST"])
def chat():

    data = request.json

    user_message = data.get("message", "").strip()
    session_id = data.get("session_id", "default")

    if not user_message:
        return jsonify({"error": "Message cannot be empty"}), 400

    session = get_or_create_session(session_id)

    session["messages"].append({
        "role": "user",
        "content": user_message
    })

    start_time = time.time()

    try:

        # Build conversation history
        prompt = ""

        for msg in session["messages"]:
            if msg["role"] == "user":
                prompt += f"User: {msg['content']}\n"
            else:
                prompt += f"Assistant: {msg['content']}\n"

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        assistant_message = response.text

        latency = round((time.time() - start_time) * 1000)

        session["messages"].append({
            "role": "assistant",
            "content": assistant_message
        })

        session["message_count"] += 1

        stats["total_messages"] += 1

        return jsonify({
            "response": assistant_message,
            "session_id": session_id,
            "latency_ms": latency,
            "input_tokens": 0,
            "output_tokens": 0,
            "model": "gemini-2.5-flash"
        })

    except Exception as e:

        if session["messages"]:
            session["messages"].pop()

        return jsonify({
            "error": str(e)
        }), 500


@app.route("/api/stats")
def get_stats():

    uptime = int(time.time() - stats["start_time"])

    return jsonify({
        "total_messages": stats["total_messages"],
        "total_tokens": stats["total_tokens"],
        "sessions_created": stats["sessions_created"],
        "active_sessions": len(chat_sessions),
        "uptime_seconds": uptime
    })


@app.route("/api/history/<session_id>")
def get_history(session_id):

    session = chat_sessions.get(session_id, {"messages": []})

    return jsonify(session["messages"])


@app.route("/api/clear/<session_id>", methods=["POST"])
def clear_session(session_id):

    if session_id in chat_sessions:
        chat_sessions[session_id]["messages"] = []
        chat_sessions[session_id]["message_count"] = 0

    return jsonify({
        "status": "cleared"
    })


if __name__ == "__main__":
    app.run(debug=True, port=5000)