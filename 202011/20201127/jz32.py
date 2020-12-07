# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        queue = [root, None]
        result, direction, child = [], True, []
        while len(queue) != 1:
            node = queue.pop(0)
            if node:
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                if direction:
                    child.append(node.val)
                else:
                    child.insert(0, node.val)
            else:
                queue.append(None)
                result.append(child)
                child = []
                direction = not direction
        result.append(child)
        return result

