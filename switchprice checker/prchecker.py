import smtplib
import pandas as pd
import requests
from bs4 import BeautifulSoup
from price_parser import Price

PRODUCT_URL_CSV = "switchprice checker/products.csv"
SAVE_TO_CSV = True
PRICES_CSV = "switchprice checker/prices.csv"
SEND_MAIL = True


def get_url(csv_file):
    df = pd.read_csv(csv_file)
    return df
def get_response(url):
    response = requests.get(url)
    return response.text

def get_price(html):
    soup = BeautifulSoup(html, "lxml")
    el = soup.select_one("p.price:nth-child(1)")
    price = Price.fromstring(el.text)
    return price.amount_float

def process_products(df):
    updated_products = []
    for product in df.to_dict("records"):
        html = get_response(product["url"])
        product["price"] = get_price(html)
        product["alert"] = product["price"] < product["alert_price"]
        updated_products.append(product)
    return pd.DataFrame(updated_products)
         
#email notifs
#def get_mail(df):
    #subject = "Price Drop Alert"
    #body = df[df["alert"]].to_string()
    #subject_and_message = f"Subject:{subject}\n\n{body}"
    #return subject_and_message

#def send_mail(df):
    #message_text = get_mail(df)
    #with smtplib.SMTP("smtp.server.address")

def main():
    df = get_url(PRODUCT_URL_CSV)
    df_updated = process_products(df)
    if SAVE_TO_CSV:
        df_updated.to_csv(PRICES_CSV,index=False, mode="a")

main()