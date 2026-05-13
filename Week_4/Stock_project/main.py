import os
import requests
from dotenv import load_dotenv
from twilio.rest import Client

#ENV
load_dotenv()

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_API_KEY = os.getenv("STOCK_API_KEY")
NEWS_API_KEY = os.getenv("NEWS_API_KEY")
TWILIO_SID = os.getenv("TWILIO_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")

#Get Yesterday's closing stock price
stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY,
}
response = requests.get(STOCK_ENDPOINT, params=stock_params)
data = response.json()["Time Series (Daily)"]
data_list = [value for (key, value) in data.items()]
yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data["4. close"]
print(f"Here's yesterday's Closing Price: {yesterday_closing_price}")

#Get the day before yesterday's closing stock price
day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price = day_before_yesterday_data["4. close"]
print(f"Here's the Day Before Yesterday Closing Price: {day_before_yesterday_closing_price}")

#Find the positive difference between 1 and 2. e.g. 40 -20 = -20, but the positive difference is 20.
difference = abs(float(yesterday_closing_price) - float(day_before_yesterday_closing_price))
up_down = None
if difference > 0:
    up_down = ""
else:
    up_down = "Down"


#Work out the percentage difference in price between closing price yesterday and,
# closing price the day before yesterday.
diff_percent = round((difference / float(yesterday_closing_price)) * 100)
print(f"Here's the Difference Percentage: %{diff_percent}")

#Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.
if diff_percent > 2:
    news_params = {
        "apiKey" : NEWS_API_KEY,
        "qInTitle": COMPANY_NAME,
    }

    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    articles = news_response.json()["articles"]

#Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation
three_articles = articles[:3]
print(f"Here's the News Articles: {three_articles}")

#Create a New list of the first 3 articles headline and description using list comprehension.
formatted_articles = [(f"{STOCK_NAME}: {up_down}{diff_percent}%\n "
                       f"headline: {article['title']}. \n"
                       f"Brief: {article['description']}") for article in three_articles]

#Send each article as a separate message via Twilio.
client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

#Send each article as a separate message via Twilio.
for article in formatted_articles:
    message = client.messages.create(
        body=article,
        from_="+Fake_Phone_Number from twilio",
        to='+your phone number'
    )
