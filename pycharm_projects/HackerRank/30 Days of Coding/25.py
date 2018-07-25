# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
def isPrime(n):
    if n == 1:
        return "Not prime"
    elif n == 2:
        return "Prime"

    elif n%2 == 0:
        return "Not prime"
    else:
        upper = int(math.sqrt(n))+1
        for i in range(3, upper, 2):
            if n%i == 0:
                return "Not prime"
        return "Prime"


input_number = input()
for i in range(input_number):
    print isPrime(input())

# print int(math.sqrt(9))
# for i in range(3, int(math.sqrt(9)), 2):
#     print i