# Question1
def howManyToInvite(A, B, a):
    # Return the number of people Leha should invite to his party
    return int(a/(float(A)/B))

def question1():
    A, B, a = input().strip().split(' ')
    A, B, a = [int(A), int(B), int(a)]
    b = howManyToInvite(A, B, a)
    print(b)

# Question2
def question2():
    n, m, k = input().strip().split(' ')
    n, m, k = [int(n), int(m), int(k)]
    coordinates = list()
    distances = list()
    for a0 in range(m):
        x, y = input().strip().split(' ')
        x, y = [int(x), int(y)]
        coordinates.append((x, y))
    # print(coordinates)
    for cur in range(0, len(coordinates)-1):
        for next in range

question2()