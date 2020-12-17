# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        if not root:
            return []

        queue, cur, count,result = [root, None], 0, 0, []
        while len(queue) != 1:
            node = queue.pop(0)
            if node:
                cur +=  node.val
                count += 1
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            else:
                queue.append(None)
                result.append(cur / count)
                cur, count = 0, 0
        result.append(cur / count)

        return result
