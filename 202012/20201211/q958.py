# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isCompleteTree(self, root: TreeNode) -> bool:
        queue = [root]
        while queue:
            node = queue.pop(0)
            if node:
                if not queue:
                    queue.append(node.left)
                elif not queue[-1] and node.left:
                    return False
                queue.append(node.left)
                if not queue:
                    queue.append(node.right)
                if not queue[-1] and node.right:
                    return False
                queue.append(node.right)

        return True

