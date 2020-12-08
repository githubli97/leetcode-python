# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def trimBST(self, root: TreeNode, low: int, high: int) -> TreeNode:
        def trim(root: TreeNode, low: int, high: int) -> TreeNode:
            if not root:
                return None
            elif root.val > high:
                return trim(root.left, low, high)
            elif root.val < low:
                return trim(root.right, low, high)
            else:
                root.left = trim(root.left, low, high)
                root.right = trim(root.right, low, high)
                return root

        return trim(root, low, high)