# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if not root:
            return None

        def leftToRight(left: TreeNode, right: TreeNode) -> TreeNode:
            if not left:
                return right
            if not right:
                return left
            copyRight = right
            while right.left:
                if right.left:
                    right = right.left
            else:
                right.left = left
            return copyRight

        if root.val == key:
            return leftToRight(root.left, root.right)

        queue = [root]
        while queue:
            node = queue.pop(0)
            if node.left:
                if node.left.val == key:
                    node.left = leftToRight(node.left.left, node.left.right)
                    return root
                queue.append(node.left)
            if node.right:
                if node.right.val == key:
                    node.right = leftToRight(node.right.left, node.right.right)
                    return root
                queue.append(node.right)
        return root