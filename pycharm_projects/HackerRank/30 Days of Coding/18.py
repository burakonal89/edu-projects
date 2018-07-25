import sys
from collections import deque

class Solution:
    # Write your code here
    def __init__(self):
        self.stack = list()
        self.queue = deque()

    def pushCharacter(self, char):
        return self.stack.append(char)

    def enqueueCharacter(self, char):
        return self.queue.append(char)

    def popCharacter(self):
        return self.stack.pop()

    def dequeueCharacter(self):
        return self.queue.popleft()


# read the string s
s=raw_input()
#Create the Solution class object
obj=Solution()

l=len(s)
# push/enqueue all the characters of string s to stack
for i in range(l):
    obj.pushCharacter(s[i])
    obj.enqueueCharacter(s[i])

isPalindrome=True
'''
pop the top character from stack
dequeue the first character from queue
compare both the characters
'''
for i in range(l / 2):
    print obj.popCharacter(), obj.dequeueCharacter()
    if obj.popCharacter()!=obj.dequeueCharacter():
        isPalindrome=False
        break
#finally print whether string s is palindrome or not.
if isPalindrome:
    sys.stdout.write ("The word, "+s+", is a palindrome.")
else:
    sys.stdout.write ("The word, "+s+", is not a palindrome.")