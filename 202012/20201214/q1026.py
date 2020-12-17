# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        stack, maxV, prev = [], 0, None
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop(-1)
            if root.right and root.right != prev:
                stack.append(root)
                root = root.right
            else:
                prev = root
                for i in stack:
                    maxV = max(maxV, abs(root.val - i.val))
                root = None
        return maxV