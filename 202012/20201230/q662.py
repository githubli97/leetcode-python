# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        if not root:
            return 0

        queue, dept, result, childMin, childMax = [root, None], 0, 1, 1, 1
        root.val = 1
        while len(queue) != 1:
            node = queue.pop(0)
            if node:
                childMax = node.val
                if node.left:
                    node.left.val = 2 * node.val
                    queue.append(node.left)
                if node.right:
                    node.right.val = 2 * node.val + 1
                    queue.append(node.right)
            else:
                result = max(result, childMax - childMin + 1)
                childMin = queue[0].val
                dept += 1
                queue.append(None)
        result = max(result, childMax - childMin + 1)
        return result
