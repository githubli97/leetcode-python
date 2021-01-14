# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def smallestFromLeaf(self, root: TreeNode) -> str:
        def childStr(root: TreeNode) -> List:
            if not root.right and not root.left:
                return [chr(root.val + 97)]
            result = []
            if root.left:
                l_child_str = childStr(root.left)
                for child in l_child_str:
                    result.append(child + chr(root.val + 97))
            if root.right:
                r_child_str = childStr(root.right)
                for child in r_child_str:
                    result.append(child + chr(root.val + 97))
            return result

        return min(childStr(root))
