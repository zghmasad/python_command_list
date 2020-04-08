from time import sleep

from bs4 import BeautifulSoup
import requests

while True:
    req = requests.get('https://www.tgju.org/')
    #print(req.content)
    soup = BeautifulSoup(req.content, 'html.parser')
    findlist = soup.findAll(class_='info-price')
    print(findlist[5].get_text())
    print(findlist[8].get_text())
    sleep(10)

