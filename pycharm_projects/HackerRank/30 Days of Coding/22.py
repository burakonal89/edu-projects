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
    def getHeight(self, root):
        if root is None:
            return -1
        print root
        return 1 + max(self.getHeight(root.left), self.getHeight(root.right))

T=int(raw_input())
myTree=Solution()
root=None
for i in range(T):
    data=int(raw_input())
    root=myTree.insert(root,data)
# print myTree
print root
height=myTree.getHeight(root)
# print height