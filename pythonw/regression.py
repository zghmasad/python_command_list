import time

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import BayesianRidge
from sklearn import metrics
import seaborn as sn
import matplotlib.pyplot as plt

# candidates = {
#     'gmat': [780, 750, 690, 710, 680, 730, 690, 720, 740, 690, 610, 690, 710, 680, 770, 610, 580, 650, 540, 590, 620,
#              600, 550, 550, 570, 670, 660, 580, 650, 660, 640, 620, 660, 660, 680, 650, 670, 580, 590, 690],
#     'gpa': [4, 3.9, 3.3, 3.7, 3.9, 3.7, 2.3, 3.3, 3.3, 1.7, 2.7, 3.7, 3.7, 3.3, 3.3, 3, 2.7, 3.7, 2.7, 2.3, 3.3, 2, 2.3,
#             2.7, 3, 3.3, 3.7, 2.3, 3.7, 3.3, 3, 2.7, 4, 3.3, 3.3, 2.3, 2.7, 3.3, 1.7, 3.7],
#     'work_experience': [3, 4, 3, 5, 4, 6, 1, 4, 5, 1, 3, 5, 6, 4, 3, 1, 4, 6, 2, 3, 2, 1, 4, 1, 2, 6, 4, 2, 6, 5, 1, 2,
#                         4, 6, 5, 1, 2, 1, 4, 5],
#     'admitted': [1, 1, 0, 1, 0, 1, 0, 1, 1, 0, 0, 1, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1,
#                  1, 0, 0, 0, 0, 1]
#     }
#
# df = pd.DataFrame(candidates, columns=['gmat', 'gpa', 'work_experience', 'admitted'])
# print(df)
# X = df[['gmat', 'gpa', 'work_experience']]
# y = df['admitted']
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.01, random_state=0)
# logistic_regression = LogisticRegression()
# logistic_regression.fit(X_train, y_train)
# y_pred = logistic_regression.predict(X_test)
# confusion_matrix = pd.crosstab(y_test, y_pred, rownames=['Actual'], colnames=['Predicted'])
# sn.heatmap(confusion_matrix, annot=True)
# print('Accuracy: ', metrics.accuracy_score(y_test, y_pred))
# plt.show()

lenght = 25000
test_percent = .0001

open_times = []
opens = []
closes = []
highs = []
lows = []
outs = []
vols = []
s11=time.time()
with open('1h.csv', 'r') as f:
    i = 0
    for line in f.readlines():
        if i == 0:
            i += 1
            continue
        s = line.split(',')
        open_times.append(float(s[0]))
        # opens.append(float(s[1]))
        # highs.append(float(s[2]))
        # lows.append(float(s[3]))
        closes.append(int(float(s[4])))
        # vols.append(float(s[5]))
        # outs.append(float(s[9]))

candidates = {
    'open_time': open_times,
    # 'open': opens,
    # 'high': highs,
    # 'low': lows,
    'close': closes,
    # 'vol': vols,
    # 'out': outs
}

df = pd.DataFrame(candidates, columns=['open_time','close'])

# print(df)
X = df[['open_time',]]
y = df['close']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_percent, random_state=0)
logistic_regression = BayesianRidge()
logistic_regression.fit(X_train, y_train)
y_pred = logistic_regression.predict(X_test)
# confusion_matrix = pd.crosstab(y_test, y_pred, rownames=['Actual'], colnames=['Predicted'])
# sn.heatmap(confusion_matrix, annot=True)
# print('Accuracy: ', metrics.accuracy_score(y_test, y_pred))
# plt.show()
print(time.time()-s11)
print(y_pred)
print(y_test)
