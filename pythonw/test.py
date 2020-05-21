import time
from poloniex import Poloniex
from time import sleep


polo = Poloniex()

while True:
    start_time = time.time()
    dic = polo('returnTicker')

    with open('btc','a') as btc:
        btc.write(dic['USDT_BTC']['last'])
    with open('ava','a') as btc:
        btc.write(dic['USDT_AVA']['last'])
    with open('eth','a') as btc:
        btc.write(dic['USDT_ETH']['last'])
    with open('trx','a') as btc:
        btc.write(dic['USDT_TRX']['last'])

    x = time.time() - start_time
    if (x < 1):
        sleep(x)
