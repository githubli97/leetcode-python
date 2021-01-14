"""
# Definition for a Node.
"""
from typing import List


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        result = []
        stack = [root]
        while stack:
            node = stack.pop(-1)
            result.insert(0, node.val)
            if node.children:
                stack += node.children
        return result
