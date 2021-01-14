# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if not root:
            return []


        child_left = self.binaryTreePaths(root.left)
        child_right = self.binaryTreePaths(root.right)

        result = child_left + child_right

        if not result:
            return [str(root.val)]
        for i in range(len(result)):
            result[i] = str(root.val) + "->" + result[i]
        return result
