from twilio.rest import Client
import requests

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCKS_API_KEY = ""
NEWS_API_KEY = ""

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"


#Twilio Data
auth_token = "658dd032052aa06de36f415ca9d80786"
account_sid = "AC44a5efe81cd4352d60877970644226e2"

stock_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "outputsize": "compact",
    "apikey": STOCKS_API_KEY,
}

news_parameters = {
    "q": COMPANY_NAME,
    "apiKey": NEWS_API_KEY,
    "page": "1"
}


response = requests.get(STOCK_ENDPOINT, params=stock_parameters)
response.raise_for_status()
stocks_data = response.json()["Time Series (Daily)"]

data_list = [value for (_, value) in stocks_data.items()]
yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data["4. close"]


day_before_yesterday = data_list[1]
day_before_closing_price = day_before_yesterday["4. close"]


difference = float(yesterday_closing_price) - float(day_before_closing_price)
up_down = None
if difference > 0:
    up_down = "🔺"
else:
    up_down = "🔻"



percentage_difference = (difference / float(yesterday_closing_price)) * 100


if percentage_difference > 5:
 
    response = requests.get(NEWS_ENDPOINT, news_parameters)
    response.raise_for_status()
    news_data = response.json()["articles"]

    three_articles = news_data[:3]

    formatted_articles = [f"{STOCK_NAME}: {up_down}{percentage_difference}%\nHeadline: {article['title']}. \nBrief: {article['description']}" for article in three_articles]

    client = Client(account_sid, auth_token)
    for article in formatted_articles:
        message = client.messages \
                        .create(
                            body=article,
                            from_='+12187890977',
                            to='+524431054555'
                        )

        print(message.status)



