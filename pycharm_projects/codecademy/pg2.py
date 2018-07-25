# -*- coding: utf-8 -*-
__author__ = "burakonal"
import random

class Model:
    def __init__(self, name):
        self.name = name

class BaseType(Model):
    def __init__(self, name, surname):
        Model.__init__(self, name)
        self.surname = surname

    def __str__(self):
        return self.name + self.surname

b = BaseType("burak", "oguz")
print b

# callback example:yi
def adder(first):
    def add(second):
        return first+second
    return add
_5adder = adder(5)
print _5adder(2)

a = (i for i in range(3))
b = (1, 2)
print type(b)

def createGenerator():
    while True:
        a = random.randint(0, 100)
        if a > 95:
            yield a
            break
        yield a
mygenerator = createGenerator()
for i in mygenerator:
    print i
