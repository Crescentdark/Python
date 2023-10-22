import json
import smtplib
import urllib.request
from datetime import datetime
from bs4 import BeautifulSoup
from email.message import EmailMessage

log = ""

def check_availability(url, phrase):
    global log
    try:
        page = urllib.request.urlopen(url)
        soup = BeautifulSoup(page,features="html.parser")

        if phrase in soup.txt:
            return True
        return False
    except:
        log += "Error parsing website"





def main():
    url = "https://www.smarty.cz/nintendo-c3851"
    phrase = "OLED"
    avaliable = check_availability(url, phrase)






    if __name__ == '__name__':
        main()
