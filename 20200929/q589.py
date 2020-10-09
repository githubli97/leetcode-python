"""
# Definition for a Node.
"""
from typing import List


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        result = []
        stack = [root]
        while len(stack) != 0:
            node = stack.pop(-1)
            if node:
                if node.children:
                    while len(node.children) != 0:
                        stack.append(node.children.pop(-1))
                result.append(node.val)
        return result