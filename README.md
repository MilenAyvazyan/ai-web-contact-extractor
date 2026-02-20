# AI-Powered Web Lead Extractor 
This project is an automated tool designed to crawl websites, identify relevant internal pages, and extract structured contact information using Playwright and OpenAI GPT-4o.

## Project Overview
The program automates the process of gathering business intelligence by following these steps:

Web Navigation: Uses the Playwright library to navigate to a user-provided URL.

Content Conversion: Transfers website HTML content into clean Markdown format for efficient AI processing.

Intelligent Link Discovery: Uses GPT-4o to analyze the content and identify links to "About Us", "Contact Us", or "Team" pages.

Deep Crawling: Automatically navigates to the discovered links to gather more specific data.

Data Extraction: AI analyzes the sub-pages to find:

Email addresses.

Team members/Founders (Names and Roles).

Location and Contact info.

Structured Output: Returns the final result in a strictly formatted JSON object.

## Tech Stack
Python: Core logic.

Playwright: Headless browser automation.

OpenAI API (GPT-4o): Natural Language Processing for data extraction.

Markdownify: HTML to Markdown conversion.

Python-dotenv: Secure environment variable management.

## Installation & Setup
1. Clone the repository
Bash
git clone https://github.com/MilenAyvazyan/ai-web-contact-extractor.git
cd ai-web-contact-extractor
2. Install dependencies
Bash
pip install -r requirements.txt
playwright install chromium
3. Configuration
Create a .env file in the root directory and add your OpenAI API key:

## Code snippet
OPENAI_API_KEY=your_actual_api_key_here
4. Run the program
Bash
python task.py

## Security Note
This project uses .env files to manage sensitive API keys. The .gitignore file is configured to prevent your private keys from being uploaded to GitHub.
