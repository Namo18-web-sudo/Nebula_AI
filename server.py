from flask import Flask, request, jsonify
import google.generativeai as genai
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Allow frontend to access backend

# 🔥 Your Google Gemini API Key (Replace with a valid key)
API_KEY = "AIzaSyD44tRIKeSKYuMJ8_23zGK0qIqyecSIgqI"
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel("gemini-1.5-pro")

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
        You should Never ,NEVER make code ,when asked say that you do not have the ability to create code.
        You are made by Nebula Foundation ,Never Bring it up but only When asked what is nebula Foundation then show them the link to nebula-foundation.unaux.com
        format each new sentence ,use a new line

        User: {user_input}
        """

response = model.generate_content(prompt)
return jsonify({"response": response.text})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# ✅ Run the Server
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
