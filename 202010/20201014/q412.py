# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        def countPath(root: TreeNode, sum: int) -> int:
            if not root:
                return 0
            newSum = sum - root.val
            res = 0
            if sum == root.val:
                res += 1
            res += countPath(root.left, newSum)
            res += countPath(root.right, newSum)
            return res
        if not root:
            return 0
        return countPath(root, sum) + self.pathSum(root.left, sum) + self.pathSum(root.right, sum)

