# -*- coding: utf-8 -*-
__author__ = "burakonal"

class Solution(object):
    def maxCount(self, m, n, ops):
        min_x = m
        min_y = n
        for op in ops:
            x = op[0]
            y = op[1]
            if x < min_x:
                min_x = x
            if y < min_y:
                min_y = y
        return min_x*min_y

m = 3
n = 3
ops = [[2,2],[3,3],[3,3],[3,3],[2,2],[3,3],[3,3],[3,3],[2,2],[3,3],[3,3],[3,3]]
solution = Solution()
print solution.maxCount(m,n,ops)


