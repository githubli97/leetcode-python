# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: TreeNode) -> TreeNode:
        def dephNode(root) -> int:
            if not root:
                return 0
            return max(dephNode(root.left), dephNode(root.right)) + 1

        leftD = dephNode(root.left)
        rightD = dephNode(root.right)
        if leftD == rightD:
            return root
        elif leftD > rightD:
            return self.lcaDeepestLeaves(root.left)
        else:
            return self.lcaDeepestLeaves(root.right)

