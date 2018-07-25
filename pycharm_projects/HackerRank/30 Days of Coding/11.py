#!/bin/python

import sys


arr = []
for arr_i in xrange(6):
   arr_temp = map(int,raw_input().strip().split(' '))
   arr.append(arr_temp)
# print arr

max = sum(arr[0][0:3]) + int(arr[1][1]) + sum(arr[2][0:3])
for i in range(4):
    for j in range(4):
        temp = sum(arr[i][j:j+3]) + int(arr[i+1][j+1]) + sum(arr[i+2][j:j+3])
        if temp > max:
            max = temp

print max

