from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        result = []
        maxCount = 0
        maxNumber = None
        while root:

            root = root.left
        update(root.left.val)
        def update

if __name__ == '__main__':
    left = TreeNode(2)
    right = TreeNode(2)
    root = TreeNode(5)
    rightright = TreeNode(20)
    right.right =rightright
    root.left = left
    root.right = right
    s = Solution()
    s.findMode(root)