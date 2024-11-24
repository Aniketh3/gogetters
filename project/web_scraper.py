import requests
from bs4 import BeautifulSoup

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

def combine_content1():
    """
    Combines the text content scraped from GoFr.dev and GitHub into a single string.
    """
    # Scrape content from GoFr.dev
    gofr_content = scrape_gofr()

    # Fetch content from a GitHub raw URL
    github_url = "https://github.com/gofr-dev/gofr/blob/development/README.md"  # Example URL
    github_content = fetch_github_text(github_url)

    # Combine both contents
    combined_content = f"{gofr_content}\n\n{github_content}".strip()
    
    if combined_content:
        print("Combined content fetched successfully!")
    else:
        print("No content found from GoFr.dev or GitHub.")
    
    return combined_content

# Example usage
if __name__ == "__main__":
    combined_result = combine_content1()
    if combined_result:
        print("Combined Content:")
        print(combined_result)  # Print the fetched content
        combine_content1()
