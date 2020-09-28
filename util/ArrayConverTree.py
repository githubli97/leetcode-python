from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
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
    tree = Solution().arrayConverTree([0,-3,9,-10,None,5])
    print(1)