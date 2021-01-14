# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        stack, prev, result = [], None, []
        while stack or root1:
            while root1:
                stack.append(root1)
                root1 = root1.left

            root1 = stack.pop(-1)

            if root1.right and not root1.right == prev:
                stack.append(root1)
                root1 = root1.right
            else:
                if not root1.left and not root1.right:
                    result.append(root1.val)
                prev = root1
                root1 = None

        while stack or root2:
            while root2:
                stack.append(root2)
                root2 = root2.left

            root2 = stack.pop(-1)

            if root2.right and not root2.right == prev:
                stack.append(root2)
                root2 = root2.right
            else:
                if not root2.left and not root2.right:
                    if not result:
                        return False
                    pop = result.pop(0)
                    if pop != root2.val:
                        return False
                prev = root2
                root2 = None

        return len(result) == 0