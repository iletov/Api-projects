from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import smtplib

WEB_URL = 'https://www.emag.bg/konzola-microsoft-xbox-series-s-rrs-00010/pd/D547D2MBM/'
USER = ""
PASSWORD = ""
TARGET_PRICE = 600
ITEM = 'Microsoft Xbox Series S'

chrome_driver_path = "C:\Development\chromedriver.exe"

service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)

web_page_url = driver.get(url=WEB_URL)

number = driver.find_element(by='xpath', value='//*[@id="main-container"]/section[3]/div/div[1]/div[2]/div/div[2]/div[2]/form[1]/div/div[1]/div[1]/div/div/div[1]/p[2]')
numb = number.text
format_number = str(numb)

price = int(format_number.split(',')[0])

message = f"{ITEM} is now available for {price}.99"


if price < TARGET_PRICE:
    print(f'{message}')
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=USER, password=PASSWORD)
        connection.sendmail(from_addr=USER,
                            to_addrs=USER,
                            msg=f"Subject:Price Alert!\n\n{message}")
