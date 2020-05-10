from time import sleep
import urllib

from bs4 import BeautifulSoup
import requests

while True:
    req = requests.get('https://www.tgju.org/')
    soup = BeautifulSoup(req.content, 'html.parser')
    findlist = soup.findAll(class_='info-price')
    print(findlist[5].get_text())
    print(findlist[8].get_text())
    sleep(10)

'''#req = requests.get('https://www.tradingview.com/symbols/BTCUSD/technicals/')
#print(req.content)
url=r'https://www.tradingview.com/symbols/BTCUSD/technicals/'
page = urllib.urlopen(url)
html_content = page.read()
rendered_content = html2text.html2text(html_content)
with open(r'pythonw\text3.html','w+') as f:
    f.write(str(rendered_content))
#soup = BeautifulSoup(req.content, 'html.parser')
#findlist = soup.findAll(class_='cell-5XzWwbDG')
#print(findlist)'''
