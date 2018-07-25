import random
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
class LinkedList:
    def __init__(self, head):
        self.head = head
        # self.head = None
    def insert(self, head, value):
        if head is None:
            head = Node(value)
        elif head.next is None:
            head.next = Node(value)
        else:
            self.insert(head.next, value)
        return head
    def reverse(self, buffer):
        previous_values = list()
        current = self.head
        previous_values.append(current.value)
        for i in range(buffer-2):
            current = current.next
            if current is None:
                raise ValueError("List lenght is shorter than reverse buffer")
            previous_values.append(current.value)
        head = current.next
        self.head = head
        temp = head.next
        head.next = None
        for value in reversed(previous_values):
            head = self.insert(head, value)
        while temp:
            head = self.insert(head, temp.value)
            temp = temp.next
    def __str__(self):
        head = self.head
        nodes = list()
        while head:
            nodes.append(str(head.value))
            head = head.next
        return "->".join(nodes)

head = Node(random.randint(0,100))
linkedList = LinkedList(head)
for i in range(9):
    head = linkedList.insert(head, random.randint(0, 100))
print linkedList
linkedList.reverse(5)
print linkedList