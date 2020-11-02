# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def longestZigZag(self, root: TreeNode) -> int:
        maxVal = 0

        def goNext(root: TreeNode, point: int, lenght: int):
            if not root:
                return
            nonlocal maxVal
            maxVal = max(lenght, maxVal)
            if point == 0:
                goNext(root.left, 1, lenght + 1)
                goNext(root.right, 0, 1)
            else:
                goNext(root.right, 0, lenght + 1)
                goNext(root.left, 1, 1)

        goNext(root, 0, 0)
        goNext(root, 1, 0)
        return maxVal
