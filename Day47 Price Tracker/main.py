import requests
import lxml
import smtplib
from bs4 import BeautifulSoup

URL = "https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1"
head = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9"
    }
MYEMAIL = "xxxxxxxxx@gmail.com"
MYPW = "xxxxxxxxxxxxx"


res = requests.get(URL, headers=head)
soup = BeautifulSoup(res.content, "lxml")
soup.prettify()

price = soup.find(class_='a-offscreen').get_text()
without_currency = float(price.split("$")[1])


def send_email(itemCost):
    with smtplib.SMTP("smtp.gmail.com", port=587)as connection:
        connection.starttls()
        connection.login(user=MYEMAIL, password=MYPW)
        connection.sendmail(from_addr=MYEMAIL, to_addrs="xxxxxxxxx.com", msg=f"Subject: Price Down \n\n price is down to {itemCost}")


with open("price.txt", 'r') as file:
    docs = float(file.read())
    if docs > without_currency:
        send_email(without_currency)
        with open("price.txt", 'w') as file1:
            file1.write(str(without_currency))




