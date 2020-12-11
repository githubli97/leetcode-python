# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:

        queue, result = [root, None], 0
        while len(queue) != 1:
            node = queue.pop(0)
            if node:
                result += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            else:
                queue.append(None)
                result = 0
        return result

