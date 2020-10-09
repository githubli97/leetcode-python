"""
# Definition for a Node.
"""
from typing import List


class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root

        stack = [None, root]
        pre = None
        while len(stack) != 1:
            node = stack.pop(0)
            if node:
                if node.left:
                    stack.append(node.left)
                if node.right:
                    stack.append(node.right)
                if pre != node:
                    pre.next = node
                    pre = pre.next
            else:
                stack.append(None)
                pre = stack[0]
        return root

    def arrayConverTree(self, nums: List[int], index=0) -> Node:
        if index >= len(nums):
            return None
        else:
            left = self.arrayConverTree(nums, 2 * index + 1)
            right = self.arrayConverTree(nums, 2 * index + 2)
        tmp = Node(nums[index])
        tmp.left = left
        tmp.right = right
        return tmp

if __name__ == '__main__':
    tree = Solution().arrayConverTree([1,2,3,4,5,None,7])
    list = Solution().connect(tree)
    print(list)