# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        if not root:
            return True

        queue, result, checkNum = [root], 0, root.val
        while queue:
            node = queue.pop(0)
            if node.left:
                if node.left.val != checkNum:
                    return False
                queue.append(node.left)
            if node.right:
                if node.right.val != checkNum:
                    return False
                queue.append(node.right)
        return True