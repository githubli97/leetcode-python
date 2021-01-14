# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def getDept(root: TreeNode):
            if not root:
                return 0
            return max(getDept(root.left), getDept(root.right)) + 1
        if not root:
            return True
        return self.isBalanced(root.left) and self.isBalanced(root.right) and abs(getDept(root.left) - getDept(root.right)) <= 1