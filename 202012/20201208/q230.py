class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        if not root:
            return 0
        stack, count = [], 0
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            node = stack.pop(-1)
            count += 1
            if count == k:
                return node.val
            if node.right:
                root = node.right
        return 0
