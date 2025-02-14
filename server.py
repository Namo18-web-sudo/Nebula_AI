from flask import Flask, request, jsonify
import google.generativeai as genai
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Allow frontend to access backend

# 🔥 Your Google API Key (Keep it safe)
API_KEY = "AIzaSyDMUGkkSZu2rvVoLwOo4VIVE4dNjFv-P3I"
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel("gemini-pro")

# ✅ Home Route (Fixes 404 Error)
@app.route("/")
def home():
    return "Nebula AI is running! 🚀 Try sending a request to /chat."

# ✅ Chatbot API Route
@app.route("/chat", methods=["POST"])
def chat():
    try:
        data = request.get_json()
        user_input = data.get("message", "")

        if not user_input:
            return jsonify({"error": "No message provided"}), 400

        response = model.generate_content(user_input)
        return jsonify({"response": response.text})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# ✅ Run the Server
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
