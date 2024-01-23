import requests
from bs4 import BeautifulSoup

def scrape_articles(topic, num_articles):
    base_url = "https://www.economist.com/"
    search_url = f"{base_url}/search?q={topic}"

    response = requests.get(search_url)
    soup = BeautifulSoup(response.text, 'html.parser')

    articles = []
    for article in soup.find_all('article')[:num_articles]:
        title = article.find('h2').get_text(strip=True)
        link = article.find('a')['href']
        content = get_article_content(base_url + link)  # Implement get_article_content function
        articles.append({'title': title, 'content': content, 'url': base_url + link})

    return articles

def get_article_content(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    content = soup.find('div', {'class': 'article-content'}).get_text(strip=True)
    return content

# Example usage
topic = "python programming"
articles = scrape_articles(topic, num_articles=5)

for article in articles:
    print(f"Title: {article['title']}")
    print(f"URL: {article['url']}")
    print(f"Content: {article['content']}\n")
