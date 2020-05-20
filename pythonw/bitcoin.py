import statistics
import time
from collections import deque

from poloniex import Poloniex
from time import sleep

period_of_observation = 10

polo = Poloniex()
queBTC = deque([])
queTRX = deque([])
queETH = deque([])
queAVA = deque([])

for _ in range(period_of_observation):
    start_time = time.time()
    dic = polo('returnTicker')
    queBTC.append(float(dic['USDT_BTC']['last']))
    queAVA.append(float(dic['USDT_AVA']['last']))
    queETH.append(float(dic['USDT_ETH']['last']))
    queTRX.append(float(dic['USDT_TRX']['last']))
    x = time.time() - start_time
    if (x < 1):
        sleep(x)
print(queBTC)

while True:
    start_time = time.time()
    dic = polo('returnTicker')
    print('min=', min(queBTC))
    print('mean=', str(statistics.mean(queBTC)))
    print(queBTC)

    queBTC.append(float(dic['USDT_BTC']['last']))
    queAVA.append(float(dic['USDT_AVA']['last']))
    queETH.append(float(dic['USDT_ETH']['last']))
    queTRX.append(float(dic['USDT_TRX']['last']))
    queBTC.popleft()
    queAVA.popleft()
    queETH.popleft()
    queTRX.popleft()


    x = time.time() - start_time
    if (x < 1):
        sleep(x)
