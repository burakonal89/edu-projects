def find_median(number_list):
    "Assuming that number_list is sorted"
    if len(number_list)%2 == 0:
        return (number_list[len(number_list)/2]+number_list[len(number_list)/2-1])/2.0
    else:
        return number_list[(len(number_list)-1)/2]
def findQuantile(input_numbers):
    if len(input_numbers)%2 == 0:
        quantile1 = int(find_median(input_numbers[:n/2]))
        quantile3 = int(find_median(input_numbers[n/2:]))
        quantile2 = (input_numbers[n/2-1]+input_numbers[n/2])/2

    else:
        quantile1 = int(find_median(input_numbers[:n/2]))
        quantile3 = int(find_median(input_numbers[n/2+1:]))
        quantile2 = input_numbers[n/2]

    return quantile1, quantile2, quantile3

n = int(raw_input())
input_numbers = [int(i) for i in raw_input().split(" ")]
input_numbers.sort()

if n%2 == 0:
    quantile1 = int(find_median(input_numbers[:n/2]))
    quantile3 = int(find_median(input_numbers[n/2:]))
    quantile2 = (input_numbers[n/2-1]+input_numbers[n/2])/2
    print quantile1
    print quantile2
    print quantile3
elif n%2 == 1:
    quantile1 = int(find_median(input_numbers[:n/2]))
    quantile3 = int(find_median(input_numbers[n/2+1:]))
    quantile2 = input_numbers[n/2]
    print quantile1
    print quantile2
    print quantile3



