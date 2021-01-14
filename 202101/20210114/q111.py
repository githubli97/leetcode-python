# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        result, queue = 1, [root, None]
        while queue:
            node = queue.pop(0)
            if node:
                if not node.left and not node.right:
                    return result
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            else:
                result += 1
                queue.append(None)

        return result