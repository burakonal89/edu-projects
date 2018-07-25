# -*- coding: utf-8 -*-
__author__ = "burakonal"
class Node:
    # Constructor to initialize the node object
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    def display(self, head):
        current = head
        while current:
            print current.data
            current = current.next
    def insert(self, head, data):
        if head is None:
            head = Node(data)
        elif head.next == None:
            head.next = Node(data)
        else:
            self.insert(head.next, data)
        return head
    def reverse(self, head, k):
        prev_list = list()
        iterator = 0
        current = head
        while current:
            prev_list.append(current.data)
            current = current.next
            iterator += 1
            if iterator == k:
                head = current


mylist= LinkedList()
T = int(input())
head = None
for i in range(T):
    data = int(input())
    head = mylist.insert(head,data)
mylist.display(head)

