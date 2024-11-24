from flask import Flask, jsonify, render_template
from content_processor import combine_content
import google.generativeai as genai
from dotenv import load_dotenv
from flask_cors import CORS
from database import save_post, get_posts
from datetime import datetime

# Load environment variables from .env file
load_dotenv()

# Initialize Flask app and CORS
app = Flask(__name__)
CORS(app)

# Function to generate content using Gemini
def generate_gemini_content(prompt, content_type="email"):
    genai.configure(api_key="AIzaSyAi8Dux6HX4CaVBtFdkRvEPsoiU_2Fc418")  # Your API Key here
    model = genai.GenerativeModel("gemini-1.5-flash")

    # Generate content based on content type (email or LinkedIn)
    if content_type == "email":
        response = model.generate_content(prompt + " combine both the trending topics and the gofr documentation contents and give me the whole CAPTIONS for the EMAIL to send to the user with the correct format and do not use bold words and also generate like a professional email")
    elif content_type == "linkedin":
        response = model.generate_content(prompt + " combine both the trending topics and the gofr documentation contents and give me a single caption for an attractive LINKEDIN post and do not use bold words and also generate like a professional linkedin post")
    elif content_type == "reddit":
        response = model.generate_content(prompt + " combine both the trending topics and the gofr documentation contents and give me a single caption for an attractive REDDIT post and do not use bold words and also generate like a professional reddit post")
    return response.text  # Return the generated content

@app.route('/')
def index():
    return render_template("index.html")

# Route for Email content generation
@app.route('/generate-email', methods=['GET'])
def generate_email_content():
    combined_result = combine_content()  # Get combined content (e.g., trending topics + GoFr docs)
    email_caption = generate_gemini_content(combined_result, content_type="email")
    return render_template('generated_content.html', content=email_caption, content_type="Email")

# Route for LinkedIn content generation
@app.route('/generate-linkedin', methods=['GET'])
def generate_linkedin_content():
    combined_result = combine_content()  # Get combined content (e.g., trending topics + GoFr docs)
    linkedin_caption = generate_gemini_content(combined_result, content_type="linkedin")
    return render_template('generated_content.html', content=linkedin_caption, content_type="LinkedIn")

@app.route('/generate-reddit', methods=['GET'])
def generate_reddit_content():
    combined_result = combine_content()  # Get combined content (e.g., trending topics + GoFr docs)
    reddit_caption = generate_gemini_content(combined_result, content_type="reddit")
    return render_template('generated_content.html', content=reddit_caption, content_type="Reddit")

# API Endpoint to fetch stored captions
@app.route('/captions', methods=['GET'])
def get_stored_captions():
    posts = get_posts()  # Fetch all posts (captions) from the database
    posts_data = [{
        "id": str(post["_id"]),  # Convert the MongoDB ObjectId to string
        "email_caption": post["content"].get("email_caption", ""),  # Get the email caption
        "linkedin_caption": post["content"].get("instagram_caption", ""),  # Get the Instagram caption
        "reddit_caption": post["content"].get("reddit_caption", ""),
        "created_at": post["content"].get("created_at", "")  # Get the creation timestamp
    } for post in posts]

    # Return the stored posts data as JSON
    return jsonify(posts_data)

if __name__ == "__main__":
    app.run(debug=True)
