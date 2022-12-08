import requests
import smtplib

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

NEWS_API_KEY = "ae704215b2f1409581bf22dc98a6ec14"
STOCK_API = "HAEOZAQ674OB8I6B"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

user = "email"
password = "password"

parameters = {
    "symbol": STOCK_NAME,
    "apikey": STOCK_API
}

news_parameters = {
    "q": COMPANY_NAME,
    "sortBy": "popularity",
    "apiKey": NEWS_API_KEY
}


stock_url = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol=TSLA&apikey="
response = requests.get(stock_url, params=parameters)
response.raise_for_status()
data = response.json()
price = data["Time Series (Daily)"]

price_diff = [value for (key, value) in price.items()][:2]
last_day = price_diff[0]
closing_price = last_day["4. close"]
# print(closing_price)

day_before = price_diff[1]["4. close"]
# print(day_before)

difference = abs(float(closing_price) - float(day_before))
# print(round(difference, 2))

percent_diff = round(float(difference)/float(closing_price)*100, 2)
print(percent_diff)

if percent_diff > 1:

    news_response = requests.get(NEWS_ENDPOINT, params=news_parameters)
    news_response.raise_for_status()
    data_news = news_response.json()["articles"]
    articles = data_news[:2]

formatted_article = [f"Headline: {article['title']}. \nBrief: {article['description']}" for article in articles]


for artcl in formatted_article:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=user, password=password)
        connection.sendmail(from_addr=user,
                            to_addrs=user,
                            msg=f"Subject:{COMPANY_NAME}\n\n{artcl.encode('utf-8')}")


