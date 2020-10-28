# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        header = prev = TreeNode()
        for i in preorder:
            prev.right = TreeNode(i)
            prev = prev.right
        header = header.right
        inorder.index()
        return header