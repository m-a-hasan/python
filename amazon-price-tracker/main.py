import requests
from bs4 import BeautifulSoup
import smtplib

buying_price = 200.0

crawl = "https://www.amazon.com/NexiGo-D90-Sony_Sensors-Emergency-Assistance/dp/B0B7Y2RH9K"

header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}

try:
    response = requests.get(crawl, headers=header)
    soup = BeautifulSoup(response.text, "html.parser")
    span = soup.find("span", {"class": "aok-offscreen"}).getText()
    price = float(str(span).strip().strip("$"))

    product = soup.find("span", {"id": "productTitle"}).getText()
    title = str(product).strip()
    msg = f"Product: {title}\nPrice: {price}\nLink: {crawl}"
    print(msg)

    if price < buying_price:
        try:
            with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(user="abid.mail.test@gmail.com", password="nytw bcus txbz kjww")
                connection.sendmail(
                    from_addr="abid.mail.test@gmail.com",
                    to_addrs="abid_mail_test@yahoo.com",
                    msg=f"Subject:Time to buy from Amazon!\n\n{msg}"
                )
        except:
            print("Failed to send email!")
except:
    print("We were banned from amazon this time. Try again after some time!")