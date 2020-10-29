# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        queueLeft, queueRight = [root], [root]
        while queueLeft:
            nodeLeft = queueLeft.pop(0)
            nodeRight = queueRight.pop(0)

            if not nodeLeft and not nodeRight:
                continue
            elif nodeLeft and nodeRight:
                if nodeLeft.val != nodeRight.val:
                    return False
            else:
                return False
            if nodeLeft:
                queueLeft.append(nodeLeft.left)
                queueLeft.append(nodeLeft.right)

            if nodeRight:
                queueRight.append(nodeRight.right)
                queueRight.append(nodeRight.left)
        return True
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
    Solution().isSymmetric(Solution().arrayConverTree([1,2,2,3,4,4,3]))