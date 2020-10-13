# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if not root:
            return True
        tmp, stack = None, [root]
        while stack:
            while root.left:
                stack.append(root.left)
                root = root.left
            node = stack.pop(-1)
            if tmp and tmp.val >= node.val:
                return False
            tmp = node
            if node.right:
                stack.append(node.right)
                root = node.right
        return True
