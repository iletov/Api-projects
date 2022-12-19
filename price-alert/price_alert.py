from bs4 import BeautifulSoup
import requests
import lxml
import smtplib


URL = 'https://www.emag.bg/konzola-microsoft-xbox-series-s-rrs-00010/pd/D547D2MBM/'
TARGET_PRICE = 600
USER = ""
PASSWORD = ""

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
    "Accept-Language": "bg,en;q=0.9,ru;q=0.8,en-GB;q=0.7",
}

response = requests.get(url=URL, headers=header)
# print(response)
web_store = response.text


soup = BeautifulSoup(web_store, 'lxml')
# print(soup.prettify())

title = soup.find(name='h1', class_='page-title').get_text()

extracted_price = soup.find(name='p', class_='product-new-price has-deal').get_text()
price = float(extracted_price.split("лв")[0].split(",")[0])

message = f"{title.split('Конзола')[1]} is now available for {price}"

if price < TARGET_PRICE:
    print(f"{title.split('Конзола')[1]} is now available for {price}")
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=USER, password=PASSWORD)
        connection.sendmail(from_addr=USER,
                            to_addrs=USER,
                            msg=f"Subject:Price Alert!\n\n{message}")

