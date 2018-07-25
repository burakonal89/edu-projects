class Difference:
    def __init__(self, a):
        self.__elements = a

    def computeDifference(self):
        maximumDifference = 0
        for i in range(len(self.__elements)):
            for j in range(i+1, len(self.__elements), 1):
                temp = abs(self.__elements[i]-self.__elements[j])
                if temp > maximumDifference:
                    maximumDifference = temp
        self.maximumDifference = maximumDifference



_ = raw_input()
a = [int(e) for e in raw_input().split(' ')]

d = Difference(a)
d.computeDifference()

print d.maximumDifference