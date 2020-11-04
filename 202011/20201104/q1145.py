# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def btreeGameWinningMove(self, root: TreeNode, n: int, x: int) -> bool:
        def countRoot(root: TreeNode) -> int:
            if not root:
                return 0
            leftCount = countRoot(root.left)
            rightCount = countRoot(root.right)
            return leftCount + rightCount + 1

        if x == root.val:
            while root.right:
                root = root.right
            if root.val == n:
                return False
            else:
                return True

        else:
            queue = [root]
            while queue:
                node = queue.pop(-1)
                if node.val == x:
                    leftC = countRoot(node.left)
                    rightC = countRoot(node.right)
                    nodeCount = leftC + rightC + 1
                    return n - rightC < rightC or n - leftC < leftC or n - nodeCount > nodeCount
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            return False