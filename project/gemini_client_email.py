from flask import Flask, jsonify
from content_processor import combine_content
import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
app = Flask(__name__)

# Function to generate content using Gemini
def generate_gemini_content(prompt):
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(prompt + " combine both the trending topics and the gofr documentation contents and give me the whole CAPTIONS for the EMAIL to send to the user")
    return response.text

# API Endpoint to get the generated captions
@app.route('/generate-captions', methods=['GET'])
def get_generated_captions():
    combined_result = combine_content()  # Get combined content (e.g., trending topics + GoFr docs)
    generated_result = generate_gemini_content(combined_result)  # Generate content using Gemini
    return jsonify({"generated_captions": generated_result})  # Return the generated captions as JSON

if __name__ == "__main__":
    app.run(debug=True)
