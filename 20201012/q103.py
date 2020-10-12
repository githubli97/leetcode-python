# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        result, stack, direction, child = [], [root, None], -1, []
        while len(stack) != 1:
            node = stack.pop(0)
            if node:
                if direction == -1:
                    child.append(node.val)
                else:
                    child.insert(0, node.val)
                if node.left:
                    stack.append(node.left)
                if node.right:
                    stack.append(node.right)
            else:
                result.append(child)
                child = []
                stack.append(None)
                direction = -1 if direction == 0 else 0
        if child:
            result.append(child)
        return result

    def arrayConverTree(self, nums: List[int], index = 0) -> TreeNode:
        if index >= len(nums):
            return None
        else:
            left = self.arrayConverTree(nums, 2 * index + 1)
            right = self.arrayConverTree(nums, 2 * index + 2)
        tmp = TreeNode(nums[index])
        tmp.left = left
        tmp.right = right
        return tmp


if __name__ == '__main__':
    print(Solution().zigzagLevelOrder(Solution().arrayConverTree([3,9,20,None,None,15,7])))