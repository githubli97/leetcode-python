# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:

        queue, result = [root, None], []
        while queue:
            node = queue.pop(0)
            flag = False
            if node:
                if node.left:
                    queue.append(node.left)
                    if result:
                        result.append(node.left.val)
                    if not result and (node.left.val == x or node.left.val == y):
                        flag = True
                        result.append(node.left.val)
                if node.right:
                    queue.append(node.right)
                    if result:
                        result.append(node.right.val)
                    if flag and (node.right.val == x or node.right.val == y):
                        return False
                    if not result and (node.right.val == x or node.right.val == y):
                        result.append(node.right.val)
            else:
                queue.append(None)
                if result:
                    if result.__contains__(x) and result.__contains__(y):
                        return True
                    return False
        return False



