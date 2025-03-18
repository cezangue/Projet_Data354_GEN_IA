import requests
from bs4 import BeautifulSoup
from langchain.schema import Document

def scrape_articles(url):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"🚨 Erreur lors de l'accès à {url} : {e}")
        return []

    soup = BeautifulSoup(response.content, 'html.parser')
    links = {a['href'] for a in soup.find_all('a', href=True)}
    
    articles = []
    for link in links:
        if any(social in link for social in ["facebook", "twitter", "linkedin", "instagram", "mailto"]):
            continue

        full_link = link if link.startswith("http") else url + link
        try:
            article_response = requests.get(full_link, timeout=10)
            article_response.raise_for_status()
            article_soup = BeautifulSoup(article_response.content, 'html.parser')

            title = article_soup.find('h1')
            title = title.get_text(strip=True) if title else "Titre non trouvé"

            content = " ".join([p.get_text(strip=True) for p in article_soup.find_all('p')])
            if content:
                articles.append(Document(page_content=f"{title}\n\n{content}", metadata={"url": full_link}))
        except requests.RequestException:
            continue
    
    return articles
