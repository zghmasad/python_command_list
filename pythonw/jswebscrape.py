from time import sleep

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

br = webdriver.Firefox()
br.get('https://www.tradingview.com/symbols/BTCUSD/technicals/')
sleep(5)
html_source = br.page_source

# with open('test.xml','w') as f:
#     f.write(html_source.decode('utf-8').encode('u2212','replace').decode('u0020'))
print(html_source)
br.get('https://www.tradingview.com/symbols/BTCUSD/technicals/')
sleep(5)
print(html_source)
br.close()