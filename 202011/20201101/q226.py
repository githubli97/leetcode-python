# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return root
        result, queue = [], [root]
        while queue:
            node = queue.pop(0)
            if node:
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                node.left, node.right = node.right, node.left
        return root