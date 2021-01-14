# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def addOneRow(self, root: TreeNode, v: int, d: int) -> TreeNode:
        if d == 1:
            node = TreeNode(v)
            node.left = root
            return node

        queue, dept = [root, None], 2
        while len(queue) != 1:
            node = queue.pop(0)
            if node:
                if node.left:
                    if d == dept:
                        new = TreeNode(v)
                        node.left, new.left = new, node.left
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                    if d == dept:
                        new = TreeNode(v)
                        node.right, new.right = new, node.right
                if not node.left:
                    if d == dept:
                        node.left = TreeNode(v)
                if not node.right:
                    if d == dept:
                        node.right = TreeNode(v)
            else:
                dept += 1
                if dept > d:
                    return root
                queue.append(None)
        return root