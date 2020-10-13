# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:

        def nodeDept(node: TreeNode) -> int:
            if not node:
                return 0
            return max(nodeDept(node.left), nodeDept(node.right)) + 1

        lDept = nodeDept(root.left)
        rDept = nodeDept(root.right)

        if lDept == rDept:
            return root
        elif lDept > rDept:
            return self.subtreeWithAllDeepest(root.left)
        else:
            return self.subtreeWithAllDeepest(root.right)