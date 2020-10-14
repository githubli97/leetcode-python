# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        if not root:
            return 0
        result, stack = 0, [root]
        while stack:
            node = stack.pop(-1)
            if node:
                if not node.left and not node.right:
                    result += node.val
                else:
                    if node.left:
                        node.left.val += node.val * 2
                        stack.append(node.left)
                    if node.right:
                        node.right.val += node.val * 2
                        stack.append(node.right)
        return result

    def arrayConverTree(self, nums: List[int], index=0) -> TreeNode:
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
    print(Solution().sumRootToLeaf(Solution().arrayConverTree([1,0,1,0,1,0,1])))