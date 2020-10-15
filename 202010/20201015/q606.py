# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def tree2str(self, t: TreeNode) -> str:
        if not t:
            return ""
        stack, result = [None, t], ""
        while stack:
            node = stack.pop(-1)
            if node:
                result += "("
                result += str(node.val)
                if node.right:
                    stack.append(None)
                    stack.append(node.right)
                if node.left:
                    stack.append(None)
                    stack.append(node.left)
                else:
                    if node.right:
                        result += "()"
            else:
                result += ")"

        return result[1: -1]


