import statistics
from matplotlib import pyplot

with open('eth', 'r') as btc:
    listy = [float(line[:-1]) for line in btc]

listx = []

for i in range(len(listy)):
    listx.append(i)

pyplot.plot(listx, listy, 'r')
pyplot.show()
v = statistics.variance(listy)
print('variance :', v)
m = statistics.mean(listy)
print('mean: ', m)
sd = statistics.stdev(listy)
print('deviant', sd)
print(m/sd)
