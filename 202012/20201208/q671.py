# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        if not root:
            return -1
        queue, result, rootVal = [root], [], root.val
        while queue:
            node = queue.pop(0)
            if rootVal != node.val:
                result.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        if result:
            result.sort()
            return result[0]
        else:
            return -1
