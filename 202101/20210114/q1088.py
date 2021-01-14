# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        if not preorder:
            return None
        root = TreeNode(preorder[0])
        if len(preorder) == 1:
            return root
        i = len(preorder)
        for k in range(1, len(preorder)):
            if preorder[k] > root.val:
                i = k
                break
        root.left = self.bstFromPreorder(preorder[1: i])
        root.right = self.bstFromPreorder(preorder[i:])
        return root