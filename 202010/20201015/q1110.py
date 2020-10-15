# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        result, node, stack, prev, constains = [], root, [], None, None
        while node or stack:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop(-1)
            if not node.right or node.right == prev:
                if constains:
                    if constains == node.left:
                        node.left = None
                    if constains == node.right:
                        node.right = None
                if node.val in to_delete:
                    if node.left:
                        result.append(node.left)
                    if node.right:
                        result.append(node.right)
                    constains = node
                    break

                prev = node
                node = None
            else:
                stack.append(node)
                node = node.right

        if root.val not in to_delete:
            result.append(root)
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
    print(Solution().delNodes(Solution().arrayConverTree([1,2,3,4,5,6,7]), [3, 5]))