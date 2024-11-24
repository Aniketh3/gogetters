import requests
import os

def post_to_linkedin(content):
    url = "https://api.linkedin.com/v2/ugcPosts"
    headers = {"Authorization": f"Bearer {os.getenv('LINKEDIN_ACCESS_TOKEN')}", "Content-Type": "application/json"}
    body = {
        "author": f"urn:li:person:{os.getenv('LINKEDIN_USER_ID')}",
        "lifecycleState": "PUBLISHED",
        "specificContent": {
            "com.linkedin.ugc.ShareContent": {
                "shareCommentary": {"text": content},
                "shareMediaCategory": "NONE",
            }
        },
        "visibility": {"com.linkedin.ugc.MemberNetworkVisibility": "PUBLIC"},
    }
    response = requests.post(url, json=body, headers=headers)
    return response.status_code == 201

def post_to_twitter(content):
    url = "https://api.twitter.com/2/tweets"
    headers = {"Authorization": f"Bearer {os.getenv('TWITTER_BEARER_TOKEN')}", "Content-Type": "application/json"}
    response = requests.post(url, json={"text": content}, headers=headers)
    return response.status_code == 201
