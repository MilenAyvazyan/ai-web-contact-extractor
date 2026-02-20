from playwright.sync_api import sync_playwright
from markdownify import markdownify as md
import openai
import re
import json
import os
from dotenv import load_dotenv
load_dotenv()


def get_markdown_content(url):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(url)
        content = page.content()  
        browser.close()

    markdown_content = md(content, heading_style="ATX")  
    return markdown_content

url = input("Please enter the website URL: ").strip()
    
if not url.startswith("http"):
    print("Invalid URL. Please include http:// or https://")
else:
    print(f"Processing {url}...")
markdown_content = get_markdown_content(url)

openai.api_key = os.getenv("OPENAI_API_KEY")
def urls_from_ai(markdown_content):
    response = openai.chat.completions.create(
        model="gpt-4o",

        messages=[
            {
                "role": "system",
                "content": "You are an assistant that extracts all valid URLs related to contact information."
            },
            {
                "role": "user",
                "content": f"Extract all URLs related to team members, founders, or contact info from the following markdown content:\n\n{markdown_content}"
            }
        ],
        max_tokens=200,
        temperature=0.2
    )
    content = response.choices[0].message.content.strip()
    return content

content = urls_from_ai(markdown_content)
print(content)

def get_links(content):
    url_pattern = r'https?://[^\s\)]+'
    l = re.findall(url_pattern, content)
    return l

links = get_links(content)

def open_links(links):
    all_content = []
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        for link in links:
            try:
                page.goto(link)
                content = page.content()  
                all_content.append(content)
            except Exception as e:
                print(f'Error with {link}: {e}')
                continue

        browser.close()

    markdown_content = [md(content, heading_style="ATX") for content in all_content]
    return markdown_content

result = open_links(links)

def infos(result):
    response_2 = openai.chat.completions.create(
        model="gpt-4o",
        response_format={ "type": "json_object" },
        messages=[
            {
                "role": "system",
                "content": "You are an assistant that extracts email addresses and references to founders, team members, locations or contact info andresult should be JSON."
            },
            {
                "role": "user",
                "content": f"Extract all email addresses or mentions of founders, team members, or contact information from the following markdown content:\n\n{result}"
            }
        ],
        max_tokens=300,
        temperature=0.3
    )
    info = response_2.choices[0].message.content
    return info

info = infos(result)
response_format ={"type":"json_object"}

json_string = info.strip("```json").strip("```").strip()
data = json.loads(json_string)

print(data)