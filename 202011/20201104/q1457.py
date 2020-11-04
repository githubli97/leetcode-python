# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: TreeNode) -> int:

        def has(root: TreeNode, parentList: List) -> int:
            leftCount, rightCount = 0, 0
            if root.val in parentList:
                parentList.remove(root.val)
            else:
                parentList.append(root.val)

            if root.left:
                leftCount = has(root.left, parentList.copy())
            if root.right:
                rightCount = has(root.right, parentList.copy())
            if not root.left and not root.right:
                if not parentList or len(parentList) == 1:
                    return 1
                else:
                    return 0
            return leftCount + rightCount
        if not root:
            return 0
        return has(root, [])

if __name__ == '__main__':
    a = [1, 2, 3, 4, 1]
    a.remove(1)
    print(a)
