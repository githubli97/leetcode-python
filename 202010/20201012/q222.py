# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def countNodes(self, root: TreeNode) -> int:
        result, stack = 0, [root]
        while stack:
            node = stack.pop(0)
            if node:
                if node.left:
                    stack.append(node.left)
                if node.right:
                    stack.append(node.right)
                result += 1
        return result
