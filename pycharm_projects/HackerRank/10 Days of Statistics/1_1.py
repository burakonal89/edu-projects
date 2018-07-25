def find_median(number_list):
    "Assuming that number_list is sorted"
    # print number_list
    if len(number_list)%2 == 0:
        return (number_list[len(number_list)/2]+number_list[len(number_list)/2-1])/2.0
    else:
        return 1.0*number_list[(len(number_list)-1)/2]
def findQuantile(number_list):
    n = len(number_list)
    if n%2 == 0:
        quantile1 = find_median(number_list[:n/2])
        quantile3 = find_median(number_list[n/2:])
        quantile2 = (number_list[n/2-1]+number_list[n/2])/2.0
        
    else:
        quantile1 = int(find_median(number_list[:n/2]))
        quantile3 = int(find_median(number_list[n/2+1:]))
        quantile2 = number_list[n/2]
    
    return quantile1, quantile2, quantile3

n = int(raw_input())
numbers = [int(i) for i in raw_input().split(" ")]
frequencies = [int(i) for i in raw_input().split(" ")]
number_list = list()
for i in range(len(numbers)):
    for j in range(frequencies[i]):
        number_list.append(numbers[i])
number_list.sort()
# print number_list
quantile1, quantile2, quantile3 = findQuantile(number_list)
result = quantile3 - quantile1
print "%.1f"%(quantile3 - quantile1)
