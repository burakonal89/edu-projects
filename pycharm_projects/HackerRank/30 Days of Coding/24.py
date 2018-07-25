class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class Solution:
    def insert(self,head,data):
        p = Node(data)
        if head==None:
            head=p
        elif head.next==None:
            head.next=p
        else:
            start=head
            while(start.next!=None):
                 start=start.next
            start.next=p
        return head
    def display(self,head):
        current = head
        while current:
            print current.data,
            current = current.next

    def removeDuplicates(self,head):
        temp = list()
        if head is None:
            return temp
        else:
            temp = [str(head.data)]
        temp_node = head
        while temp_node.next:
            temp_node = temp_node.next
            if not str(temp_node.data) in temp:
                temp.append(str(temp_node.data))
        print " ".join(temp)

mylist= Solution()
T=int(input())
head=None
for i in range(T):
    data=int(input())
    head=mylist.insert(head,data)
head=mylist.removeDuplicates(head)
mylist.display(head);