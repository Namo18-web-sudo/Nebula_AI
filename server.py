from flask import Flask, request, jsonify
import google.generativeai as genai
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Allow frontend to access backend

# 🔥 Replace with your API key
API_KEY = "AIzaSyDMUGkkSZu2rvVoLwOo4VIVE4dNjFv-P3I"
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel("gemini-pro")

@app.route("/chat", methods=["POST"])
def chat():
    try:
        data = request.get_json()
        user_input = data.get("message", "")

        response = model.generate_content(user_input)
        return jsonify({"response": response.text})
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
