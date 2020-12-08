# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if not root:
            return 0

        queue, result = [root], 0
        while queue:
            node = queue.pop(0)
            if node.left:
                if not node.left.left and not node.left.right:
                    result += node.left.val
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return result
