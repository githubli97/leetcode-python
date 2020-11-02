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
        stack, prev = [root], None
        while stack:
            while root.left:
                stack.append(root.left)
                root = root.left
            node = stack.pop(-1)
            print(node.val)
            if node.right:
                stack.append(node.right)
                root = node.right
            if prev:
                if node.val <= prev.val:
                    return False
            prev = node
        return True

