import requests
import datetime as dt
import html


TICKER = "TSLA"
COMPANY_NAME = "Tesla"

# API
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
NEWS_API = "dc0c54fcf03943848c624bcb6bd8f752"

# set parameters for request.get()
news_params = {
    "apiKey": NEWS_API,
    "qInTitle": COMPANY_NAME,
    "qInContent": TICKER,
    "sortBy": "publishedAt",
    "from": dt.datetime.today().date()
}

# get news articles from api source
resp = requests.get(NEWS_ENDPOINT, params=news_params)
resp.raise_for_status()
article_list = resp.json()['articles']

# create new list of articles using list comprehension
formatted_article_list = [
    f"{TICKER} \nPublished on {article['publishedAt'].split('T')[0]} by {article['source']['name']} \nHeadline: {article['title']} \n{html.unescape(article['description'])} \n{article['url']}" for article in article_list
]

# print articles from list
for article in formatted_article_list:
    print(article,'\n')
