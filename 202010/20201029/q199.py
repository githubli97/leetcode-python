# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return []

        result, queue = [root.val], [root, None]
        while len(queue) != 1:
            node = queue.pop(0)
            if node:
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            else:
                if queue:
                    result.append(queue[-1].val)
                queue.append(None)
        return result


