# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        def hasTarget(root: TreeNode, p: TreeNode, q: TreeNode) -> (int, TreeNode):
            if not root:
                return 0, None
            hasCount, result = 0, None
            if root.val == p.val or root.val == q.val:
                hasCount,result  = 1, root
            leftHasCount, resultLeft = hasTarget(root.left, p, q)
            rightHasCount, resultRight = hasTarget(root.right, p, q)

            if leftHasCount == 2:
                return 2, resultLeft
            elif rightHasCount == 2:
                return 2, resultRight
            elif leftHasCount + rightHasCount == 2:
                return 2, root
            elif leftHasCount + rightHasCount + hasCount == 2:
                return 2, root
            elif leftHasCount:
                return leftHasCount, None
            elif rightHasCount:
                return rightHasCount, None
            elif hasCount:
                return hasCount, None
            else:
                return 0, None

        return hasTarget(root, p, q)[1]





