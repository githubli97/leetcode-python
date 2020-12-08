# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        if not root:
            return 0
        queue, result = [root], 0
        while queue:
            node = queue.pop(-1)
            flag = node.val % 2 == 0
            if node.left:
                queue.append(node.left)
                if flag:
                    if node.left.left:
                        result += node.left.left.val
                    if node.left.right:
                        result += node.left.right.val
            if node.right:
                queue.append(node.right)
                if flag:
                    if node.right.left:
                        result += node.right.left.val
                    if node.right.right:
                        result += node.right.right.val
        return result