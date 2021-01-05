# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
from typing import List


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if not nums:
            return None

        length = len(nums)
        if length == 1:
            return TreeNode(nums[0])
        elif length == 2:
            child = TreeNode(nums[0])
            cur = TreeNode(nums[1])
            cur.left = child
            return cur
        else:
            leftNode = self.sortedArrayToBST(nums[0: length // 2])
            rightNode = self.sortedArrayToBST(nums[length // 2 + 1: length])
            cur = TreeNode(nums[length // 2])
            cur.left = leftNode
            cur.right = rightNode
            return cur