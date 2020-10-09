# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        result, stack = [], [root]
        while len(stack) != 0:
            while root.left:
               stack.append(root.left)
               root = root.left
            node = stack.pop(-1)
            result.append(node.val)
            if node.right:
                stack.append(node.right)
                root = node.right
        return result



