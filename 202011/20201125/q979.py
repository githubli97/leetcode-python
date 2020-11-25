# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def distributeCoins(self, root: TreeNode) -> int:

        def getGold(root: TreeNode) -> (int, int):
            if not root:
                return 0, 0

            goldLeft, deptLeft = getGold(root.left)
            goldRight, deptRight = getGold(root.right)

            gold = goldLeft + goldRight + root.val - 1
            dept = deptLeft + deptRight + abs(gold)
            return gold, dept

        return getGold(root)[1]
