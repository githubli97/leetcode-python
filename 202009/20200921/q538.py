# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        if root is None:
            return root
        self.selectTree(root, 0)
        return root
    def selectTree(self, root: TreeNode, addNum: int) -> int:
        if root.right:
            addNum = self.selectTree(root.right, addNum)
        root.val += addNum
        addNum = root.val
        if root.left:
            addNum = self.selectTree(root.left, addNum)
        return addNum


if __name__ == '__main__':
    left = TreeNode(2)
    right = TreeNode(13)
    root = TreeNode(5)
    rightright = TreeNode(20)
    right.right =rightright
    root.left = left
    root.right = right
    s = Solution()
    s.convertBST(root)
    print("1")
