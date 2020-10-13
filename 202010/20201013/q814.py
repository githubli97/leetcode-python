# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def pruneTree(self, root: TreeNode) -> TreeNode:
        def isCutNode(root: TreeNode) -> bool:
            if not root:
                return True
            if root.val == 1:
                return False
            return isCutNode(root.left) and isCutNode(root.right)

        if isCutNode(root.left):
            root.left = None
        else:
            self.pruneTree(root.left)
        if isCutNode(root.right):
            root.right = None
        else:
            self.pruneTree(root.right)

        if root and not root.left and not root.right and root.val == 0:
            return None
        else:
            return root