# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def listOfDepth(self, tree: TreeNode) -> List[ListNode]:
        result = []
        stack = [None, tree]
        pre = None
        while len(stack) != 1:
            node = stack.pop(0)
            if not node:
                stack.append(None)
                pre = ListNode(-1)
                result.append(pre)
            else:
                pre.next = ListNode(node.val)
                pre = pre.next
                if node.left:
                    stack.append(node.left)
                if node.right:
                    stack.append(node.right)
        for i in range(len(result)):
            result[i] = result[i].next

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
    tree = Solution().arrayConverTree([1,2,3,4,5,None,7,8])
    list = Solution().listOfDepth(tree)
    print(list)



