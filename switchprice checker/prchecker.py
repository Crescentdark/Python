import smtplib
import pandas as pd
import requests
from bs4 import BeautifulSoup
from price_parser import Price

PRODUCT_URL_CSV = "products.csv"
SAVE_TO_CSV = True
PRICES_CSV = "prices.csv"
SEND_MAIL = True


def get_url(csv_file):
    df = pd.read_csv(csv_file)
    return dif