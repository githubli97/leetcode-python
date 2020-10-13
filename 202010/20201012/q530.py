# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        min, stack, pre = None, [root], None
        if root.left:
            min = abs(root.val - root.left.val)
        if root.right:
            min = abs(root.val - root.right.val)
        while len(stack) != 0:
            while root.left:
                stack.append(root.left)
                root = root.left
            node = stack.pop(-1)
            if not pre:
                pre = node
            else:
                if min > abs(node.val - pre.val):
                    min = abs(node.val - pre.val)
                pre = node
            if node.right:
                stack.append(node.right)
                root = node.right
        return min