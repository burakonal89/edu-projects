n = int(raw_input())
numbers = [int(i) for i in raw_input().split(" ")]
weights = [int(i) for i in raw_input().split(" ")]
sum = 0.0
weight_sum = 0
for i in range(n):
    sum += numbers[i]*weights[i]
    weight_sum += weights[i]
print "%2.f"%(sum/weight_sum)