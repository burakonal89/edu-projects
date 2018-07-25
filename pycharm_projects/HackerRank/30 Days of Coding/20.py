#!/bin/python

import sys


n = int(raw_input().strip())
a = map(int,raw_input().strip().split(' '))
# n = 3
# a = [2,3,1]

def swap(arr, a, b):
    i, j = arr.index(a), arr.index(b)
    arr[i], arr[j] = arr[j], arr[i]
    return arr

numberOfSwaps = 0
for i in range(1, n, 1):
    for j in range(0, i, 1):
        if a[j] > a[i]:
            # print a[i], a[j]
            swap(a, a[i], a[j])
            numberOfSwaps += 1
            # print a
    # if numberOfSwaps == 0:
    #     break
# print a
print "Array is sorted in {0} swaps.".format(numberOfSwaps)
print "First Element: {0}".format(a[0])
print "Last Element: {0}".format(a[-1])

