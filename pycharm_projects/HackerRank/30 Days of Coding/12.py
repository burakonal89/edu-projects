class Person:
    def __init__(self, firstName, lastName, idNumber):
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNumber
    def printPerson(self):
        print "Name:", self.lastName + ",", self.firstName
        print "ID:", self.idNumber

class Student(Person):

    def __init__(self, firstName, lastName, idNumber, score):
        Person.__init__(self, firstName, lastName, idNumber)
        self.score = score

    def calculate(self):
        avg_score = float(sum(self.score))/len(self.score)
        if avg_score >= 90:
            return "O"
        elif avg_score >= 80:
            return "E"
        elif avg_score >= 70:
            return "A"
        elif avg_score >= 55:
            return "P"
        elif avg_score >= 40:
            return "D"
        else:
            return "T"

line = raw_input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(raw_input()) # not needed for Python
scores = map(int, raw_input().split())
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print "Grade:", s.calculate()