import smtplib
from bs4 import BeautifulSoup
import requests


URL = ""
TARGET_PRICE = 250
EMAIL = ""
PASSWORD = ""
SMTP_ADDRESS = "smtp.gmail.com"


headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:103.0) Gecko/20100101 Firefox/103.0",
    "Accept-Language": "en-US,en;q=0.5"
}

#Request to Amazon website
response = requests.get(URL, headers=headers )
amazon_product = response.text


#Scraping the price
soup = BeautifulSoup(amazon_product, "lxml")
price = float(soup.find(name="span", class_="a-price-whole").getText())


#Sending notification email
title = soup.find(id="productTitle").get_text().strip()
if price < TARGET_PRICE:
    message = f"{title} is now {price}"

    with smtplib.SMTP(SMTP_ADDRESS, port=587) as connection:
        connection.starttls()
        result = connection.login(EMAIL, PASSWORD)
        connection.sendmail(
            from_addr=EMAIL,
            to_addrs=EMAIL,
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{URL}"
        )
