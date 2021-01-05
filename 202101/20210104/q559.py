"""
# Definition for a Node.
"""
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0

        maxV = 0
        for i in root.children:
            maxV = max(maxV, self.maxDepth(i))
        return maxV + 1

