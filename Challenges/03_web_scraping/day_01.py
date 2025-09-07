import requests
import json
from bs4 import BeautifulSoup


URL = "https://docs.chaicode.com/youtube/getting-started/"

def get_h2_headers(url):
    try:
        response = requests.get(url,timeout=10)
        response.raise_for_status()  # Check for HTTP errors
  

    except requests.RequestException as e:
        print(f"Error fetching the URL: {e}")
        
        
    soup = BeautifulSoup(response.text,'html.parser')  
    print(soup.prettify())  
    h2_tags = soup.find_all('h2')
    print(h2_tags)
    headers = []
    for tag in h2_tags:
        headers_text = tag.get_text(strip=True)
        if headers_text and headers_text.lower() != "contents":
            headers.append(headers_text)

    print(headers)

get_h2_headers(URL)