from pytrends.request import TrendReq

def fetch_trending_searches():
    # Initialize pytrends
    pytrends = TrendReq(hl='en-US', tz=360)
    
    try:
        # Get the trending searches globally
        trending_searches = pytrends.trending_searches(pn='united_states')  # You can change this to a different region
        
        print("Trending Searches:")
        print(trending_searches.head(20))  # Print top 20 trending searches
        
        return trending_searches.head(20)  # Return the top 20 trending searches
        
    except Exception as e:
        print(f"Error occurred: {str(e)}")
        return ["Error occurred while fetching trending searches."]

# Fetch and print the trending searches
trending = fetch_trending_searches()
print("Top Trending Searches:", trending)