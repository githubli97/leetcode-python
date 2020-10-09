# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthLargest(self, root: TreeNode, k: int) -> int:
        if not root:
            return 0
        result, stack, count = TreeNode(), [root], 0
        pre = result
        while len(stack) != 0:
            while root.right:
               stack.append(root.right)
               root = root.right
            node = stack.pop(-1)
            if node.left:
                stack.append(node.left)
                root = node.left
            count += 1
            if count == k:
                return node.val
        return 0


