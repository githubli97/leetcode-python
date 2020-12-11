# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:
        stack, prev, minV = [], None, None
        while stack or root:
            while root:
                stack.append(root)
                root = root.left

            node = stack.pop(-1)
            if prev:
                if minV:
                    minV = min(minV, node.val - prev)
                else:
                    minV = node.val - prev

            prev = node.val

            if node.right:
                root = node.right

        return minV
