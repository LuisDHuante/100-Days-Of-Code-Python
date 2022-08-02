from bs4 import BeautifulSoup
import requests


response = requests.get(
    "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")

empire_web_page = response.text
soup = BeautifulSoup(empire_web_page, "html.parser")


titles = soup.find_all("h3")

title_texts = []


for title in titles:
    text = title.getText()
    title_texts.append(text)


with open("movies.txt", "w", encoding='utf8') as f:
    for movie in title_texts:
        f.write(f"{movie}\n")

