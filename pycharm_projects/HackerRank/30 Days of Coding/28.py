import sys


t = int(raw_input().strip())
for a0 in xrange(t):
    max = 0
    n, k = raw_input().strip().split(' ')
    n, k = [int(n), int(k)]
    for i in range(1, n, 1):
        for j in range(i+1, n+1, 1):
            temp = i&j
            if temp > max and temp < k:
                max = temp
            if temp == k:
                break
    print max
