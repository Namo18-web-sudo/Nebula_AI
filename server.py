from flask import Flask, request, jsonify
import google.generativeai as genai
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# 🔥 Your Google Gemini API Key
API_KEY = "AIzaSyDMUGkkSZu2rvVoLwOo4VIVE4dNjFv-P3I"
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel("gemini-pro")

# ✅ Home Route
@app.route("/")
def home():
    return "Nebula AI is running! 🚀 Try sending a request to /chat."

# ✅ Chatbot API Route with System Instructions
@app.route("/chat", methods=["POST"])
def chat():
    try:
        data = request.get_json()
        user_input = data.get("message", "")

        if not user_input:
            return jsonify({"error": "No message provided"}), 400

        # 🔥 Add system instructions to make it act as Nebula AI
        prompt = f"""
        You are Nebula AI, a powerful and friendly chatbot. 
        Always introduce yourself as 'Nebula AI' and not 'Gemini'.
        Keep responses clear and engaging.
        
        User: {user_input}
        """

        response = model.generate_content(prompt)
        return jsonify({"response": response.text})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# ✅ Run the Server
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

        return jsonify({"error": str(e)}), 500

# ✅ Run the Server
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
