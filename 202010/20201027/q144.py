# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        result, stack = [], [root]
        if not root:
            return result

        while stack:
            node = stack.pop(-1)
            if node:
                if node.right:
                    stack.append(node.right)
                if node.left:
                    stack.append(node.left)
            result.append(node.val)
        return result


