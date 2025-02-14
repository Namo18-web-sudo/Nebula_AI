from flask import Flask, request, jsonify
import google.generativeai as genai
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

API_KEY = "YOUR_GEMINI_API_KEY"  # Replace with your actual API key
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel("gemini-pro")

@app.route("/")
def home():
    return "Nebula AI is running! 🚀 Try sending a request to /chat."

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
        return jsonify({"error": str(e)}), 500  # ✅ Correctly indented!

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

