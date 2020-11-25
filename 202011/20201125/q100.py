# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        def compareNode(p: TreeNode, q: TreeNode) ->bool:
            if p and q and p.val == q.val:
                return True
            elif not q and not p:
                return True
            else:
                return False

        queueP, queueQ = [p], [q]
        while queueP or queueQ:
            if not queueP or not queueQ:
                return False

            p = queueP.pop(0)
            q = queueQ.pop(0)
            if not compareNode(p, q):
                return False
            if p:
                queueP.append(p.left)
                queueP.append(p.right)
            if q:
                queueQ.append(q.left)
                queueQ.append(q.right)
        return True