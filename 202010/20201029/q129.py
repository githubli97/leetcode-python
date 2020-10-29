# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        if not root:
            return 0
        def sumNumbers(root: TreeNode, parentNumber: int) -> int:
            parentNumber *= 10
            parentNumber += root.val
            if not root.left and not root.right:
                return parentNumber
            elif root.left and root.right:
                leftNumber = sumNumbers(root.left, parentNumber)
                rightNumber = sumNumbers(root.right, parentNumber)
                return leftNumber + rightNumber
            elif root.right:
                return sumNumbers(root.right, parentNumber)
            else:
                return sumNumbers(root.left, parentNumber)
        return sumNumbers(root, 0)
