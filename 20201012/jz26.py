# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:
        result, stackA = False, [A]
        if not A or not B:
            return result

        while stackA:
            nodeA = stackA.pop(0)
            if nodeA:
                if nodeA.left:
                    stackA.append(nodeA.left)
                if nodeA.right:
                    stackA.append(nodeA.right)

                stackAA, stackB = [nodeA], [B]
                while stackB:
                    if not stackAA:
                        break
                    nodeB = stackB.pop(0)
                    nodeAA = stackAA.pop(0)
                    if nodeB and not nodeAA:
                        break
                    elif nodeB:
                        if nodeAA.val != nodeB.val:
                            break
                        if nodeB.left:
                            stackB.append(nodeB.left)
                            if nodeAA.left:
                                stackAA.append(nodeAA.left)
                        if nodeB.right:
                            stackB.append(nodeB.right)
                            if nodeAA.right:
                                stackAA.append(nodeAA.right)
                else:
                    return True
        return result