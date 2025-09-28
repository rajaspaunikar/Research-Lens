import requests
from bs4 import BeautifulSoup

def scrape_arxiv_titles():
    url = "https://arxiv.org/list/cs/recent"  # recent computer science papers
    response = requests.get(url)
    if response.status_code != 200:
        print("Failed to retrieve page")
        return
    
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Titles are in <div class="list-title mathjax">
    titles = soup.find_all('div', class_='list-title mathjax')
    
    print("Recent arXiv CS Paper Titles:\n")
    for t in titles:
        # The text contains "Title:" prefix, remove it and strip whitespace
        title = t.text.replace('Title:', '').strip()
        print(title)

if __name__ == "__main__":
    scrape_arxiv_titles()
