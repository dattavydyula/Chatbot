from flask import Flask, request, jsonify
import subprocess
import json

app = Flask(__name__)

def chat_with_ollama(prompt):
    cmd = ["ollama", "run", "llama3", prompt]
    process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, _ = process.communicate()
    return output.decode("utf-8")

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message", "")
    if not user_message:
        return jsonify({"reply": "Please send a message."})
    
    reply = chat_with_ollama(user_message)
    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
