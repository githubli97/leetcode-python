# Definition for a binary tree node.
import copy
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        if n == 0:
            return None
        if n == 1:
            return [TreeNode(1)]
        result = []
        for i in range(1, n + 1):
            childList = []
            root = TreeNode(i)
            leftList = self.generateTrees(i - 1)
            rightList = self.generateTrees(n - i)
            if leftList and rightList:
                for childRoot in leftList:
                    copy_root = copy.deepcopy(root)
                    copy_root.left = childRoot
                    childList.append(copy_root)
                for childRoot in childList:
                    for rightRoot in rightList:
                        deepcopy = copy.deepcopy(childRoot)
                        deepcopyRight = copy.deepcopy(rightRoot)
                        deepcopy.right = deepcopyRight
                        queue = [deepcopyRight]
                        while queue:
                            node = queue.pop(0)
                            node.val += i

                            if node.left:
                                queue.append(node.left)
                            if node.right:
                                queue.append(node.right)
                        result.append(deepcopy)
            elif leftList:
                for childRoot in leftList:
                    copy_root = copy.deepcopy(root)
                    copy_root.left = childRoot
                    result.append(copy_root)
            elif rightList:
                for childRoot in rightList:
                    queue = [childRoot]
                    while queue:
                        node = queue.pop(0)
                        node.val += 1

                        if node.left:
                            queue.append(node.left)
                        if node.right:
                            queue.append(node.right)
                    copy_root = copy.deepcopy(root)
                    copy_root.right = childRoot
                    result.append(copy_root)
        return result

if __name__ == '__main__':
    Solution().generateTrees(5)

