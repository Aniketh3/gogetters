# GoGetters: AI-Driven Content Automation

GoGetters is a streamlined solution designed to automate the creation and outreach of content for social media and email campaigns. By harnessing the power of AI and natural language processing (NLP), it simplifies digital engagement and content workflows.

## Features

- **Web Scraping**: Extracts relevant data from `GoFr.dev` for content generation.
- **Trend Analysis**: Uses NLP to analyze and incorporate social media trends.
- **AI-Powered Content Creation**: Generates customized posts and email templates with Google Gemini API.
- **Cold Email Automation**: Automates the generation of personalized cold emails.
- **Social Media Integration**: Schedules and posts AI-generated content on various social platforms.

## Project Structure

```
project/
├── static/                # Static assets for the project
├── templates/             # HTML templates
├── .gitignore             # Git ignored files
├── app.py                 # Entry point for the application
├── content_processor.py   # Content processing logic
├── database.py            # Handles data storage and retrieval
├── gemini_client_email.py # Gemini API integration for email content
├── gemini_client_instagram.py # Gemini API integration for Instagram content
├── generate_cold_emails.py # Cold email generation module
├── social_media.py        # Social media posting logic
├── trend_fetcher.py       # NLP-based trend analysis
├── web_scraper.py         # Web scraping logic for GoFr.dev
```

## What It Does

GoGetters automates the process of creating and sharing content, saving time and ensuring high-quality output. It:

1. Scrapes data from GoFr.dev to find relevant topics.
2. Analyzes trends using NLP models like SpaCy or Hugging Face.
3. Uses Google Gemini API to create engaging posts and email templates.
4. Automates the scheduling of posts and outreach emails, simplifying the workflow.

---
