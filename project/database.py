from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

# Connect to MongoDB and specify the database and collection
client = MongoClient(os.getenv("MONGO_URI"))
db = client.gofr  # This connects to the "gofr" database
posts_collection = db.posts  # This refers to the "posts" collection within the database

# Function to save a post (email and Instagram captions)
def save_post(content):
    posts_collection.insert_one({"content": content, "status": "pending"})  # Save with status "pending"

# Function to retrieve all posts
def get_posts():
    return list(posts_collection.find())  # Fetch all documents in the posts collection
