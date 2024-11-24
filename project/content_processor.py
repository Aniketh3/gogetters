import requests
from bs4 import BeautifulSoup
from trend_fetcher import fetch_trending_searches  # Assuming this module provides trending search functionality
from web_scraper import combine_content1  # Assuming this module contains the first scraping logic

def scrape_gofr():
    """
    Scrapes text content from GoFr.dev by fetching all <p> tags.
    """
    url = "https://gofr.dev"  # Replace with actual URL
    response = requests.get(url)
    
    if response.status_code == 200:
        print("Request successful for GoFr.dev!")
        soup = BeautifulSoup(response.content, "html.parser")
        
        # Scrape all <p> tags and join their text content
        paragraphs = soup.find_all("p")
        text_content = "\n".join([p.text.strip() for p in paragraphs if p.text.strip()])
        
        if text_content:
            print("GoFr.dev content fetched successfully!")
            return text_content
        else:
            print("No content found in <p> tags on GoFr.dev.")
            return ""
    else:
        print(f"Failed to fetch GoFr.dev content. Status code: {response.status_code}")
        return ""

def fetch_github_text(repo_url):
    """
    Fetches plain text from a GitHub raw file URL.
    Filters out unnecessary content like badges, HTML tags, etc.
    """
    # Convert GitHub URL to raw URL
    raw_url = repo_url.replace("github.com", "raw.githubusercontent.com").replace("/blob/", "/")
    
    response = requests.get(raw_url)
    
    if response.status_code == 200:
        print("Request successful for GitHub raw content!")
        
        # Extract raw text content and clean unnecessary sections
        raw_text = response.text.strip()
        cleaned_text = "\n".join(line.strip() for line in raw_text.splitlines() if line.strip())
        
        return cleaned_text
    else:
        print(f"Failed to fetch GitHub content. Status code: {response.status_code}")
        return ""

def combine_content():
    """
    Combines the text content scraped from GoFr.dev and GitHub into a single string.
    """
    # Fetch trending searches
    trending_searches = fetch_trending_searches()
    
    # Scrape content from GoFr.dev and GitHub
    gofr_content = scrape_gofr()
    github_url = "https://github.com/gofr-dev/gofr/blob/development/README.md"  # Example URL
    github_content = fetch_github_text(github_url)

    # Combine all contents
    combined_content = (
        f"Top Trending Searches:\n{trending_searches}\n\n"
        f"GoFr.dev Content:\n{gofr_content}\n\n"
        f"GitHub Content:\n{github_content}"
    ).strip()
    
    if combined_content:
        print("Combined content fetched successfully!")
    else:
        print("No content found from any source.")
    
    return combined_content

if __name__ == "__main__":
    # Call the function and print the result
    combined_result = combine_content()
    print(combined_result)  # Print the final combined content
    combine_content()
