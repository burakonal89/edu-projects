import math
def findMean(numbers):

    return float(sum(numbers)/len(numbers))

def findVariance(numbers):

    mean = findMean(numbers)
    sum = 0.0
    for number in numbers:
        sum += (number-mean)**2
    return math.sqrt(sum/len(numbers))
n = raw_input()
numbers = [int(i) for i in raw_input().split(" ")]
print "%.1f"%findVariance(numbers)