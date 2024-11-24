# from trend_fetcher import fetch_trending_searches
# from web_scraper import scrape_gofr
from content_processor import combine_content
import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables from .env file
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

# Function to combine content
# def combine_content():
#     # Fetch trending searches
#     trending_searches = fetch_trending_searches()
    
#     # Scrape website content
#     scraped_content = scrape_gofr()
    
#     # Combine both results
#     combined_content = (
#         f"Top Trending Searches:\n{trending_searches}\n\n"
#         f"Website Content:\n{scraped_content}"
#     )
    
#     return combined_content  # Return the combined content

# Function to generate content using Gemini
def generate_gemini_content(prompt):
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(prompt + "combine both the trending topics and the gofr documentation contents and give me the captions for the INSTAGRAM POST")
    print("This was called")
    print(response.text)
    return response.text

if __name__ == "__main__":
    # Call the function to combine content
    combined_result = combine_content()
    
    # Pass the combined content as a prompt to Gemini
    print("Combined Content:")
    print(combined_result)

    generated_result = generate_gemini_content(combined_result)

    # Print the generated content from Gemini
    print("\nGenerated Content from Gemini:")
    print(generated_result)
