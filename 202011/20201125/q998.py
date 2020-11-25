# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def insertIntoMaxTree(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            return None

        if root.val < val:
            newNode = TreeNode(val)
            newNode.left = root
            return newNode

        copyRoot = root

        while root and root.val > val and root.right:
            if root.right.val < val:
                newNode = TreeNode(val)
                root.right, newNode.left = newNode, root.right
                return copyRoot
            root = root.right
        newNode = TreeNode(val)

        root.right = newNode
        return copyRoot