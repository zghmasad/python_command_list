import time
from poloniex import Poloniex
from time import sleep
import pandas


polo = Poloniex()
with open('orderbook','w+') as orbf:
    orbf.write(str(polo.returnOrderBook(currencyPair='USDT_BTT',depth=10)))
# print(polo.returnOrderBook(currencyPair='USDT_BTC',depth=10))

# while True:
#     start_time = time.time()
#     dic = polo('returnTicker')
#
#     with open('btc','a') as btc:
#         btc.write(dic['USDT_BTC']['last'])
#     with open('ava','a') as btc:
#         btc.write(dic['USDT_AVA']['last'])
#     with open('eth','a') as btc:
#         btc.write(dic['USDT_ETH']['last'])
#     with open('trx','a') as btc:
#         btc.write(dic['USDT_TRX']['last'])
#
#     x = time.time() - start_time
#     if (x < 1):
#         sleep(x)
