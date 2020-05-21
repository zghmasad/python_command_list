import statistics
import time
from collections import deque

from poloniex import Poloniex
from time import sleep


# declaration phase ---------------------------------------------------
class Step:
    def __init__(self):
        self.count = 0
        self.percent = 0
        self.last_price = float(0)

# time of period of observation
period_of_observation = 10

# poloniex object
polo = Poloniex()

# queues declaration
queBTC = deque([])
queTRX = deque([])
queETH = deque([])
queAVA = deque([])


# initiation phase------------------------------------------------------
dic = polo('returnTicker')
first_step=Step()
# BTC---------------------
first_step.last_price=float(dic['USDT_BTC']['last'])
queBTC.append(first_step)
# AVA---------------------
first_step.last_price=float(dic['USDT_AVA']['last'])
queAVA.append(first_step)
# TRX---------------------
first_step.last_price=float(dic['USDT_TRX']['last'])
queTRX.append(first_step)
# ETH---------------------
first_step.last_price=float(dic['USDT_ETH']['last'])
queETH.append(first_step)

for _ in range(period_of_observation):
    start_time = time.time()
    dic = polo('returnTicker')
    # BTC ----------------
    newstep=Step()
    newstep.last_price=float(dic['USDT_BTC']['last'])
    laststep=queBTC[-1]
    newstep.percent=(newstep.last_price-laststep.last_price)/laststep.last_price
    if newstep.percent*laststep.percent>0:
        pass
    else:
        pass
    queBTC.append(newstep)
    # AVA ----------------
    queAVA.append(float(dic['USDT_AVA']['last']))

    # ETH ----------------
    queETH.append(float(dic['USDT_ETH']['last']))

    # TRX ----------------
    queTRX.append(float(dic['USDT_TRX']['last']))
    x = time.time() - start_time
    if (x < 1):
        sleep(x)
print(queBTC)



# main phase -----------------------------------------------------------
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
