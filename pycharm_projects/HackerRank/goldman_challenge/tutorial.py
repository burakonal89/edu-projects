def profit(lst):
    indices = [i for i, j in sorted(enumerate(lst), key=lambda (i, j): j, reverse=True)]

    sell = []
    for i in indices:
        if not sell or i > sell[-1]:
            sell.append(i)

    it = iter(sell)
    # print sell
    next_best = next(it)
    stock = 0
    money = 0
    # debug = []
    for i, price in enumerate(lst):
        if i < next_best:
            stock += 1
            money -= price
        if i == next_best:
            money += stock * price
            stock = 0
            next_best = next(it, -1)

            # debug.append((money, stock, i, next_best, price))
    return money

def read_array(file):
    tests = []
    with open(file) as f:
        n = int(f.readline().strip())
        for i in range(n):
            lst = [int(x) for x in f.readline().strip().split()]
            tests.append(lst)
    return tests

tests = read_array('test_case')
    max_ = test[-1]
    profit = 0
    max_ = 0
    for price in reversed(test[1:]):

# if __name__ == "__main__":
#     tests = []
#     with open('test_case') as f:
#         n = int(f.readline().strip())
#         for i in range(n):
#             lst = [int(x) for x in f.readline().strip().split()]
#             tests.append(lst)
#
#     for arr in tests:
#         print(profit(arr))

    # for arr in tests:
    #     profit = 0
    #     for i in range(len(arr)-1):
    #         max_ = 0
    #         for j in range(i+1, len(arr)):
    #             temp = arr[j] - arr[i]
    #             if temp > max_:
    #                 max_ = temp
    #         profit += max_
    #     print(profit)