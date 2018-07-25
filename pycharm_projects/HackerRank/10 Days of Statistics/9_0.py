# -*- coding: utf-8 -*-
__author__ = "burakonal"

from sklearn import linear_model

m, n = raw_input().split(" ")
m = int(m)
n = int(n)
features = list()
results = list()
for i in range(n):
    line = raw_input().split(" ")
    results.append(float(line[-1]))
    temp = list()
    for num in line[:-1]:
        temp.append(float(num))
    features.append(temp)
n = int(raw_input())
observations = list()
for i in range(n):
    line = raw_input().split(" ")
    observations.append([float(x) for x in line])
print features
print results
print observations

lm = linear_model.LinearRegression()
lm.fit(features, results)
predictions = lm.predict(observations)
for prediction in predictions:
    print "%.2f" % prediction
