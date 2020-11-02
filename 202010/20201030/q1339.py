# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxProduct(self, root: TreeNode) -> int:
        rootCopy = root
        stack, prev, result = [], None, []
        while root or stack:
            while root:
                stack.append(root)
                root = root.left

            root = stack.pop(-1)
            if not root.right or prev == root.right:
                if root.left:
                    root.val += root.left.val
                if root.right:
                    root.val += root.right.val
                result.append(root.val)
                prev = root
                root = None
            else:
                stack.append(root)
                root = root.right

        minAbs = rootCopy.val
        nodeValue = 0
        for i in range(len(result)):
            if minAbs > abs(rootCopy.val/2 - result[i]):
                minAbs = abs(rootCopy.val/2 - result[i])
                nodeValue = result[i]

        return (rootCopy.val-nodeValue) * nodeValue % 1000000007