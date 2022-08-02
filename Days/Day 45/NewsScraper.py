from bs4 import BeautifulSoup
import requests


response = requests.get("https://news.ycombinator.com/news")

yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")
articles = soup.find_all(name="a", class_= "titlelink")
article_texts = []
article_links = []

for article_tag in articles:
    text = article_tag.getText()
    article_texts.append(text)

    link = article_tag.get("href")
    article_links.append(link)


article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]

# print(article_texts)
# print(article_links)
# print(article_upvotes)


highest_voted = article_upvotes.index(max(article_upvotes))
print(article_texts[highest_voted])
print(article_links[highest_voted])


