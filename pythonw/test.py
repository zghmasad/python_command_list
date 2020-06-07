# from poloniex import Poloniex
from matplotlib import pyplot
import openpyxl


def prob(list, amount):
    count = 0
    for i in list:
        if i > amount:
            count += 1
    return count, count / len(list)

def probneg(list, amount):
    count = 0
    for i in list:
        if i < amount:
            count += 1
    return count, count / len(list)


def countlist(list,amount):
    list2=[]
    for i in list:
        if i > amount:
            list2.append(list.index(i))
    return list2

def countlistneg(list,amount):
    list2=[]
    for i in list:
        if i < amount:
            list2.append(list.index(i))
    return list2


# polo = Poloniex()
# pairsAll=polo.returnOrderBook(currencyPair='USDT_BTC',depth=100)
# pairs=pairsAll['bids']
# pairs.sort(key=lambda pair: pair[0])
# for p in pairs:
#     print(p)
#
# # print(pairs)
# print(polo.returnOrderBook(currencyPair='USDT_BTC', depth=50))

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
# import statistics
#
# from matplotlib import pyplot
#
#
# listy = [1, 1, 1, 1, 1]
# listy5 = [0, 0, 0, 0, 0]
# with open('btc', 'r') as f:
#     i = 0
#     for line in f:
#         listy.append(float(line[:-1]))
#         listy5.append((listy[i + 5] - listy[i]) / listy[i + 5])
#         i += 1
#
# listy5[0] = 0
# listy5[1] = 0
# listy5[2] = 0
# listy5[3] = 0
# listy5[4] = 0
# listx = [i for i in range(len(listy5))]
#
# # pyplot.plot(listx, listy5, 'g')
# # pyplot.plot(listx, listy[5:], 'k')
# # pyplot.show()
# print(min(listy5))
# print(max(listy5))
#
# print(sorted(listy5))

def file_to_list(url):
    l = []

    with open(url, 'r') as f:
        for line in f:
            l.append(float(line[:-1]))

    return l


def devi(list1, count):
    min1 = 10000
    max1 = -10000
    mean1 = 0
    l = []
    for i in range(count, len(list1)):
        element = ((list1[i - count] - list1[i]) * 100) / list1[i - count]
        l.append(element)
        mean1 += element
        if element < min1:
            min1 = element
        if element > max1:
            max1 = element
    return l, min1, max1, (mean1 / len(l))


print('creating list ...')
list5 = file_to_list('btc')
listp, min1, max1, mean1 = devi(list5, 120)
# print(min1, max1, mean1)
# c,p=prob(listp, .6)
# print(float(p),c)
# c,p=probneg(listp, -.6)
# print(float(p),c)
print('list created!')
listxx=countlistneg(listp,-3.7)
print('new list')
print(listxx)
listx = [i for i in range(len(list5))]

pyplot.plot(listx, list5, 'g')
pyplot.show()

# xlsx------------------------------------------------------------
# wk=openpyxl.load_workbook('Book1.xlsx')
# ws=wk.active
# # listt=[0,.4,-.4,.5,-.5,.6,-.6,.7,-.7,.8,-.8,.9,-.9,1,-1,1.1,-1.1,1.2,-1.2,1.3,-1.3,1.4,-1.4,1.5,-1.5,1.6,-1.6,1.7,-1.7,1.8,-1.8,1.9,-1.9,2,-2]
# # ws.append(listt)
# for j in (10,20,30,45,60,120,240,480,960):
#     listp, min1, max1, mean1 = devi(list5, j)
#     listt=[j]
#     for i in range(4,300):
#         percent=float(i)/10
#         c, p = prob(listp, percent)
#         cn, pn = probneg(listp, -percent)
#         if c==0 and cn==0:
#             break
#         listt.append(c)
#         listt.append(cn)
#     ws.append(listt)
#     listt.clear()
#
# wk.save('Book1.xlsx')