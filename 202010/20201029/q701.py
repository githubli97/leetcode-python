# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        newNode = TreeNode(val)
        if not root:
            return newNode
        prev = root
        while True:
            if prev.val > val:
                if prev.left:
                    prev = prev.left
                else:
                    prev.left = newNode
                    break
            else:
                if prev.right:
                    prev = prev.right
                else:
                    prev.right = newNode
                    break
        return root