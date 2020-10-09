# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        result, stack = TreeNode(), [root]
        pre = result
        while len(stack) != 0:
            while root.left:
               stack.append(root.left)
               root = root.left
            node = stack.pop(-1)
            if node.right:
                stack.append(node.right)
                root = node.right
            pre.right = node
            pre.left = None
            pre = pre.right
        return result.right



