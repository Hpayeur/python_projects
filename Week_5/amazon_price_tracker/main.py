from bs4 import BeautifulSoup
from dotenv import load_dotenv
import smtplib
import os
import requests

load_dotenv()

url = "https://www.amazon.com/gp/aw/d/B0BGHV69X5/?"

#header
header = {
    "Accept": "text/html,application/xhtml=xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "en-GB,de;q=0.8,fr;q=0.6,en;q0.4,ja;q=0.2",
    "Cookie": 'COOKIEINFO',
    "Priority": "u=1",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "none",
    "Sec-Fetch-User": "?1",
    "Sec-Gpc": "1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:126.0) Gecko/20100101 Firefox/126.0",
}

# Requests
response = requests.get(url, headers=header)
soup = BeautifulSoup(response.content, "html.parser")

price_as_float = None

# The Price!
price = soup.find(
    name="span",
    class_="a-offscreen",
)
if price:
    price = price.get_text()
    price_without_currency = price.split("$")[1]
    price_as_float = float(price_without_currency)
    print(price_as_float)
else:
    print("No price found or Available at this moment")

#Send an Email
title = soup.find(name="span", id="productTitle")
if title:
    title = title.get_text().strip()
    print(title)
else:
    print("This title doesn't exist")

BUY_PRICE = 20

if price_as_float is not None and price_as_float < BUY_PRICE:
    message = f"{title} is finally on sale for {price}"

    # Variables
    with smtplib.SMTP(os.environ["SMIP_ADDRESS"], port=587) as connection:
        connection.starttls()
        result = connection.login(os.environ["EMAIL_ADDRESS"], os.environ["EMAIL_PASSWORD"])
        connection.sendmail(
            from_addr=os.environ["EMAIL_ADDRESS"],
            to_addrs=os.environ["EMAIL_ADDRESS"],
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{url}".encode("utf-8")
        )
