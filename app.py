from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

OLLAMA_URL = "http://localhost:11434/api/generate"

def get_response(user_input):
    payload = {
        "model": "phi3:mini",   # lightweight model
        "prompt": user_input,
        "stream": False
    }

    response = requests.post(OLLAMA_URL, json=payload)
    return response.json()["response"]

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    user_input = data.get("message")

    reply = get_response(user_input)

    return jsonify({
        "input": user_input,
        "response": reply
    })

if __name__ == "__main__":
    app.run(debug=True)