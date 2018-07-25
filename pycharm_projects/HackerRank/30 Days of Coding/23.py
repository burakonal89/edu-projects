import sys

class Node:
    def __init__(self,data):
        self.right=self.left=None
        self.data = data
    def __str__(self):
        return str(self.data)
class Solution:
    def insert(self,root,data):
        if root==None:
            return Node(data)
        else:
            if data<=root.data:
                cur=self.insert(root.left,data)
                root.left=cur
            else:
                cur=self.insert(root.right,data)
                root.right=cur
        return root
    def levelOrder(self,root):
        temp = ""
        if root:
            queue = [root]
        else:
            queue = list()
        while queue:
            node = queue.pop()
            temp += str(node.data)+" "
            if node.left:
                queue.insert(0,node.left)
            if node.right:
                queue.insert(0,node.right)
        print temp




T=int(raw_input())
myTree=Solution()
root=None
for i in range(T):
    data=int(raw_input())
    root=myTree.insert(root,data)
myTree.levelOrder(root)