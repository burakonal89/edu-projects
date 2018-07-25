#!/bin/python
import sys
n = int(raw_input().strip())
n_bin = bin(n)[2:]

# print n_bin
max_1 = 1
flag_1 = False
count_1 = 0
# print n_bin
# print type(n_bin)
for i in n_bin:
    if i == "0":
        count_1 = 0
        flag_1 = False

    elif i == "1":
        if flag_1 is True:
            count_1 += 1
        else:
            flag_1 = True
            count_1 = 1
    if count_1 > max_1:
        max_1 = count_1

print max_1