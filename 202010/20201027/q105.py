# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if len(preorder) != len(inorder) or len(preorder) == 0:
            return None
        rootValue = preorder.pop(0)
        rootIndex = inorder.index(rootValue)
        root = TreeNode(rootValue)
        left = self.buildTree(preorder[0: rootIndex], inorder[0: rootIndex])
        right = self.buildTree(preorder[rootIndex: len(preorder)], inorder[rootIndex + 1: len(inorder)])
        root.left = left
        root.right = right
        return root







if __name__ == '__main__':
    root = Solution().buildTree([3,9,20,15,7], [9,3,15,20,7])
    print(root)
