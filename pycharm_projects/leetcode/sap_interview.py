# -*- coding: utf-8 -*-
__author__ = "burakonal"
import random

# Q1)
# given a sorted array with possibly having repetitive elements:
a = [1, 1, 2, 3, 4, 5, 6, 6, 6, 7, 8, 9, 10, 10]


# sum should be 55
# find the sum of the elements

def find_sum(a):
    prev = a[0]
    sum = prev
    for current in a[1:]:
        if current != prev:
            sum += current
        prev = current
    return sum


# print find_sum(a)


# Q2)

# Example:
# Inputs:  1->2->3->4->5->6->7->8->NULL and k = 3
# Output:  3->2->1->6->5->4->8->7->NULL.
#
# Inputs:   1->2->3->4->5->6->7->8->NULL and k = 5
# Output:  5->4->3->2->1->8->7->6->NULL.

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value):
        self.head = Node(value)

    def insert(self, head, value):
        # if head is None:
        #     self.head = Node(value)
        if head.next is None:
            head.next = Node(value)
        else:
            self.insert(head.next, value)
        return head
    def revese(self, k):
        pass

    def __str__(self):
        head = self.head
        items = list()
        while head is not None:
            items.append(str(head.value))
            head = head.next
        return "->".join(items)

random_list = [random.randint(0, 100) for i in range(10)]
print random_list
head_value = random_list[0]
linkedList = LinkedList(head_value)
head = linkedList.head
for i in random_list[1:]:
    linkedList.insert(head, i)
print linkedList

