# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        result = []
        if not root:
            return result
        stack = [None, root]
        level = None
        while len(stack) != 1:
            node = stack.pop(0)
            if node:
                level.append(node.val)
                if node.left:
                    stack.append(node.left)
                if node.right:
                    stack.append(node.right)
            else:
               result.append(level)
               level = []
               stack.append(None)
        else:
            result.append(level)
        result.pop(0)
        return result
