from flask import Flask, render_template, request, jsonify
from langdetect import detect
import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()  # Load environment variables

API_KEY = os.getenv("GEMINI_API_KEY")  # Retrieve the key from .env
if not API_KEY:
    raise ValueError("API_KEY not found. Please check your .env file.")

# Configure Gemini with the API key
genai.configure(api_key=API_KEY)

# Initialize Flask
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json["message"]

    # Detect language
    try:
        lang = detect(user_message)
    except:
        lang = "en"

    # If the message is in French, respond in English to say that only English is supported
    if lang == "fr":
        response = "Sorry, I only support English for now. Please ask in English."
    else:
        response = generate_response(user_message)

    return jsonify({"response": response})

def generate_response(user_input):
    """ Send request to Gemini and retrieve the response """
    try:
        model = genai.GenerativeModel("gemini-1.5-flash")  # Fast and free model
        response = model.generate_content(user_input)
        return response.text
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == "__main__":
    app.run(debug=True)
