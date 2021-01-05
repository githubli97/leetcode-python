# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def printTree(self, root: TreeNode) -> List[List[str]]:
        if not root:
            return []

        array, child, dept, queue, flag = [], [], 1, [root], True
        result = []
        while queue:
            node = queue.pop(0)
            if node:
                child.append(node.val)
                queue.append(node.left)
                queue.append(node.right)
                flag = False
            else:
                queue.append(None)
                queue.append(None)
                child.append(None)

            if len(child) == pow(2, dept - 1):
                if flag:
                    break
                flag = True
                dept += 1
                array.append(child)
                child = []

        dept -= 1
        long = pow(2, dept) -1
        for i in range(dept):
            result.append([])
            start = pow(2, dept - i - 1) - 1
            step = pow(2, dept - i)
            count = 0
            for j in range(long):
                if j == start:
                    if array[i][count] == 0 or array[i][count]:
                        result[i].append(str(array[i][count]))
                    else:
                        result[i].append("")
                    count += 1
                    start += step
                else:
                    result[i].append("")
        return result




