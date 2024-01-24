import requests
from bs4 import BeautifulSoup

def scrape_articles(topic, num_articles):
    base_url = "https://www.nytimes.com"
    search_url = f"{base_url}/search?dropmab=false&query={topic}&sort=best"
    # print(search_url,"\n")

    response = requests.get(search_url)
    soup = BeautifulSoup(response.text, 'html.parser')

    articles = []
    findall=soup.find_all('li')
    # print(findall[1].find('h4', class_='css-2fgx4k').get_text(strip=True))
    for i in range(1, num_articles-1):
        try:
            title = findall[i].find('h4', class_='css-2fgx4k').get_text(strip=True)
            # print("title:",title)
            link = findall[i].find('a')['href']
            # print("link:",link)
            # content = get_article_content(base_url + link)  # Implement get_article_content function
            # print("content",content)
            articles.append((title, base_url+link, topic))
        except:
            print("Fail on ",topic)
    # print(articles)
    return articles

def get_article_content(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    content = soup.find('div', class_='css-1gb49t4').get_text(strip=True)
    print("content ",content)
    return content

# Example usage
topics = ["Tesla", "Microsoft", "Amazon", "BlackRock", "SNP500", "Meta", "global-economy"]
all_articles=[]
for topic in topics:
    # print("Scraping for " + topic + "\n")
    articles = scrape_articles(topic, 5)
    all_articles.extend(articles)

print("\n",len(all_articles), "Articles found:\n")
for article in all_articles:
    print("Topic: ", article[2])
    print("Title: ",article[0])
    print("URL: ", article[1],"\n")
