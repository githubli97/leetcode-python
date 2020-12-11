# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        def deptMax(root:TreeNode) -> int:
            if not root:
                return -1
            return max(deptMax(root.left), deptMax(root.right)) + 1

        if not root:
            return 0
        deptLeft = deptMax(root.left)
        deptRight = deptMax(root.right)
        return max(self.diameterOfBinaryTree(root.left), self.diameterOfBinaryTree(root.right), deptRight + deptLeft + 2)