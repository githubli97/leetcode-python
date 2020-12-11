# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        if not root:
            return False
        queue, nodeList = [root], []
        while queue:
            node = queue.pop(0)
            nodeList.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        while nodeList:
            node = nodeList.pop(0)
            if nodeList.__contains__(k - node):
                return True
        return False

if __name__ == '__main__':
    print(Solution().findTarget([]))