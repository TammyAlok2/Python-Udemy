import requests
import csv
from bs4 import BeautifulSoup

HN_URL = "https://delhihighcourt.nic.in/"
CSV_FILE = "hn_top20.csv"

def fetch_top_post():
    try:
        response = requests.get(HN_URL, timeout=10)
        response.raise_for_status()  # Check for HTTP errors
    except requests.RequestException as e:
        print(f"Error fetching the URL: {e}")
        return None
    soup = BeautifulSoup(response.text, 'html.parser')
    print(soup)
    post_links = soup.select("span.titleline > a ")
    print(post_links)
    
    posts = []
    for link in post_links[:20]:
        title = link.text.strip()
        url = link.get('href').strip()
        posts.append({"title": title, "url": url})
        
    return posts


def save_to_csv(posts, filename):
    if not posts :
        print("No posts to save.")
        return
    
    with open(filename,"w",newline='',encoding='utf-8') as file:
        writer = csv.DictWriter(file,fieldnames=["title","url"])  
        writer.writeheader()
        writer.writerows(posts)
        
    print(f"Data saved to {filename}")    
            
    
    
def main():
    print("Scraping Hacker News top posts...  ")
    posts =  fetch_top_post()
    print("collected all data")
    save_to_csv(posts, CSV_FILE)
    
    
if __name__ == "__main__":
    main()   
    

