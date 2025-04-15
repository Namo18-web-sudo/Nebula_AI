from flask import Flask, request, jsonify
import google.generativeai as genai
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Allow frontend to access backend

# 🔥 Your Google Gemini API Key (Replace with a valid key)
API_KEY = "AIzaSyBN-98TJb5V26b5TqZl-OxFRSrRohlHp4U"
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel("gemini-pro")

# ✅ Home Route (Fixes 404 Error)
@app.route("/")
def home():
    return "Nebula AI is running! 🚀 Try sending a request to /chat."

# ✅ Chatbot API Route with Custom Personality
@app.route("/chat", methods=["POST"])
def chat():
    try:
        data = request.get_json()
        user_input = data.get("message", "")

        if not user_input:
            return jsonify({"error": "No message provided"}), 400

        # 🔥 Custom system prompt to force AI identity as Nebula AI
        prompt = f"""
        You are Nebula AI, an advanced AI assistant created to help users.
        You are **not** made by Google.
        Stay professional, engaging, and helpful in your responses.
        Only say your name when you are asked but never say it othervise
        You should **Never** ,NEVER make code ,when asked say that you do not have the ability to create code.
        User: {user_input}
        """

        response = model.generate_content(prompt)
        return jsonify({"response": response.text})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# ✅ Run the Server
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
