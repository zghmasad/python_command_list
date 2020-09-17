#!/usr/bin/python3
import json
import time

import requests

# i=0
# j=0
# btc_list=[]
# text=''
# while True:
#     s=time.time()
#     req = requests.get('https://api.binance.com/api/v3/ticker/price')
#     s2=time.time()
#     try:
#         jsonobj = json.loads(req.text)
#         btc_list.append((jsonobj[11]['price'],#btc
#                          jsonobj[12]['price'],#eth
#                          jsonobj[308]['price'],#xrp
#                          jsonobj[326]['price'],#eos
#                          jsonobj[353]['price'],#trx
#                          s2))
#     except:
#         print('get url error')
#     if s2-s<1:
#         time.sleep(s2 - s)
#
#     i+=1
#     if i>100000:
#         for l in btc_list:
#             text+=l[0] + ',' +l[1] + ',' +l[2] + ',' +l[3] + ',' +l[4] + ',' + str(l[5]) + '\n'
#         with open('btcNew', 'a') as btc:
#             btc.write(text)
#         text=''
#         i=0
#         btc_list.clear()

# first=1582600000000
first=1_502_942_400_000
# end=1600081200000
# distance=97,138,800,000
for i in range(28):
    s1=time.time()
    first+=3_600_000_000
    second=first+3_600_000_000-1
    req = requests.get('https://api.binance.com/api/v1/klines?symbol=BTCUSDT&interval=1h&startTime='+str(first)+'&endTime='+str(second)+'&limit=1000')
    json1=json.loads(req.text)
    with open('1h.csv','a') as f:
        for j in json1:
            f.write(str(j[0])+','+str(j[1])+','+str(j[2])+','+str(j[3])+','+str(j[4])+','+str(j[5])+','+str(j[6])+'\n')
    s2=time.time()-s1
    if s2<1:
        time.sleep(1-s2)

# def candels_high(candels):
#     h=0
#     for candel in candels:
#         if candel['open']>h:
#             h=candel['open']
#         if candel['close']>h:
#             h=candel['close']
#     return h
#
# def candels_low(candels):
#     l = 100000000000000
#     for candel in candels:
#         if candel['open'] < l:
#             l = candel['open']
#         if candel['close'] < l:
#             l=candel['close']
#     return l
#
#
# candels_1m=[]
#
# with open('1m.csv','r') as r:
#     lines=r.readlines()
#     for line in lines:
#         s=line.split(',')
#         candels_1m.append({'open_time':float(s[0]),'open':float(s[1]),'high':float(s[2]),'low':float(s[3]),'close':float(s[4]),'close_time':float(s[5])})
#
# # with open('test2.xml' , 'w') as f:
# #     f.write(str(candels_1m))
#
# three_line_break_5m=[]
# renko_1m=[]
#
# if candels_1m[0]['open'] < candels_1m[0]['close']:
#     temp = {'open': candels_1m[0]['open'], 'close': candels_1m[0]['close'], 'color': 'green'}
# else:
#     temp = {'open': candels_1m[0]['close'], 'close': candels_1m[0]['open'], 'color': 'red'}
# renko_1m.append(temp)
#
#
#
#
# for i in range(len(candels_1m)):
#
