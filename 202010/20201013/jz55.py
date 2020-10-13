# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            return False
        def nodeDept(node: TreeNode) -> int:
            if not node:
                return 0
            return max(nodeDept(node.left), nodeDept(node.right)) + 1
        return abs(nodeDept(root.left) - nodeDept(root.right)) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)