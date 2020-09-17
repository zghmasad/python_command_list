'''
three line break with open and close
'''
import json

import pandas
from matplotlib.patches import Rectangle
from matplotlib import pyplot
import requests
from matplotlib.pyplot import figure


def renko(jsonobject,pipsize=None):
    renko_list = []
    opens_list = []
    close_list = []
    lows_list = []
    highs_list = []
    # open_times = []
    three_line_break = []
    for j in jsonobject:
        # open_times.append(float(j[0]) / 60000)  # convert to minutes
        opens_list.append(float(j[1]))  # open
        highs_list.append(float(j[2]))  # high
        lows_list.append(float(j[3]))  # low
        close_list.append(float(j[4]))  # close
    if len(opens_list)<=15:
        return

    # url = 'https://api.binance.com/api/v3/ticker/price'
    # req = requests.get(url)
    # jsonobj = json.loads(req.text)
    # l = float(jsonobj[11]['price'])
    list1=[max(highs_list[i]-lows_list[i],abs(highs_list[i]-close_list[i-1]),abs(lows_list[i]-close_list[i-1])) for i in range(-15,-1)]
    if pipsize==None:
        # pipsize=(sum(highs_list[-14:])-sum(lows_list[-14:]))/15
        pipsize=sum(list1)/14
        # pipsize-=pipsize*.1
        print(pipsize)

    if opens_list[0] < close_list[0]:
        temp = {'open': opens_list[0], 'close': close_list[0], 'color': 'green'}
    else:
        temp = {'open': close_list[0], 'close': opens_list[0], 'color': 'red'}
        # temp = {'open': opens_list[0], 'close': close_list[0], 'color': 'red'}
    renko_list.append(temp)
    for i in range(1,len(close_list)):
        if renko_list[-1]['color']=='green':
            if renko_list[-1]['close']<close_list[i]:
                las=renko_list[-1]['close']
                for j in range(int((close_list[i]-las)/pipsize)):
                    open2=renko_list[-1]['close']
                    close2=open2+pipsize
                    renko_list.append({'open': open2, 'close': close2, 'color': 'green'})

            if renko_list[-1]['open']>close_list[i]:
                las=renko_list[-1]['open']
                for j in range(int((las-close_list[i])/pipsize)):
                    if j==0:
                        open2=renko_list[-1]['open']
                    else:
                        open2=renko_list[-1]['close']
                    close2=open2-pipsize
                    renko_list.append({'open': open2, 'close': close2, 'color': 'red'})


        if renko_list[-1]['color']=='red':
            if renko_list[-1]['close']>close_list[i]:
                las=renko_list[-1]['close']
                for j in range(int((las-close_list[i])/pipsize)):
                    open2=renko_list[-1]['close']
                    close2=open2-pipsize
                    renko_list.append({'open': open2, 'close': close2, 'color': 'red'})

            if renko_list[-1]['open']<close_list[i]:
                las=renko_list[-1]['open']
                for j in range(int((close_list[i]-las)/pipsize)):
                    if j==0:
                        open2=renko_list[-1]['open']
                    else:
                        open2=renko_list[-1]['close']
                    close2=open2+pipsize
                    renko_list.append({'open': open2, 'close': close2, 'color': 'green'})
    # renko_list


    del renko_list[0]
    return renko_list

def candels_high(candels):
    h=0
    for candel in candels:
        if candel['open']>h:
            h=candel['open']
        if candel['close']>h:
            h=candel['close']
    return h

def candels_low(candels):
    l = 100000000000000
    for candel in candels:
        if candel['open'] < l:
            l = candel['open']
        if candel['close'] < l:
            l=candel['close']
    return l

def ThreeLineBreak(jsonobject):
    # highs_list = []
    opens_list = []
    close_list = []
    # lows_list = []
    # open_times = []
    three_line_break = []
    for j in jsonobject:
        # open_times.append(float(j[0]) / 60000)  # convert to minutes
        opens_list.append(float(j[1]))  # open
        # opens_list.append(float(j[2]))  # high
        # close_list.append(float(j[3]))  # low
        close_list.append(float(j[4]))  # close

    if len(opens_list)<=10:
        return

    if opens_list[0]<close_list[0]:
        temp={'open':opens_list[0],'close':close_list[0],'color':'green'}
    else:
        temp={'open':close_list[0],'close':opens_list[0],'color':'red'}
    three_line_break.append(temp)
    three_line_break.append(temp)
    three_line_break.append(temp)


    for i in range(1, len(opens_list)):
        if three_line_break[-1]['color'] == 'green':
            if close_list[i]>three_line_break[-1]['close']:
                three_line_break.append({'open':three_line_break[-1]['close'],'close':close_list[i],'color':'green'})
            elif close_list[i]<candels_low(three_line_break[-3:]):
                three_line_break.append({'open':three_line_break[-1]['open'],'close':close_list[i],'color':'red'})

        if three_line_break[-1]['color'] == 'red':
            if close_list[i]<three_line_break[-1]['close']:
                three_line_break.append({'open':three_line_break[-1]['close'],'close':close_list[i],'color':'red'})
            elif close_list[i]>candels_high(three_line_break[-3:]):
                three_line_break.append({'open':three_line_break[-1]['open'],'close':close_list[i],'color':'green'})
    del three_line_break[:2]
    return three_line_break

def chart_plot(candels):
    currentAxis = pyplot.gca()
    # max1 = candels[0]['close']
    # min1 = candels[0]['open']
    j=100
    for i in candels:
        j+=1
        if i['color']=='green':
            currentAxis.add_patch(Rectangle((j, i['open']), 1, i['close'] - i['open'], facecolor="green"))
        else:
            currentAxis.add_patch(Rectangle((j, i['close']), 1, i['open'] - i['close'], facecolor="red"))
    currentAxis.set_xlim(99, 220)
    currentAxis.set_ylim(8000, 14000)
    pyplot.show()
#
#
req = requests.get('https://api.binance.com/api/v1/klines?symbol=BTCUSDT&interval=1m&limit=1000')
json1 = json.loads(req.text)
print(json1)
# l=ThreeLineBreak(json1)
# chart_plot(l[-100:])
l=renko(json1)
chart_plot(l[-100:])
# print(l)
# print(json1)




# open_times=opens_list=highs_list=lows_list=close_list=[]
#
# for j in json1:
#         open_times.append(float(j[0]) / 60000)  # convert to minutes
#         opens_list.append(float(j[1]))  # open
#         highs_list.append(float(j[2]))  # high
#         lows_list.append(float(j[3]))  # low
#         close_list.append(float(j[4]))  # close


