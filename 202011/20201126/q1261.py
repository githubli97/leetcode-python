# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class FindElements:

    def __init__(self, root: TreeNode):
        if not root:
            return None

        queue, root.val = [root], 0
        while queue:
            node = queue.pop(0)
            if node.left:
                queue.append(node.left)
                node.left.val = 2 * node.val + 1
            if node.right:
                queue.append(node.right)
                node.right.val = 2 * node.val + 2
        self.root = root

    def find(self, target: int) -> bool:

        queue = [target]
        while target != 0:
            if target % 2:
                target = (target - 1) / 2
            else:
                target = (target - 2) / 2
            if not target:
                break
            queue.insert(0, target)

        root = self.root
        while queue:
            node = queue.pop(0)
            if root:
                if root.left and root.left.val == node:
                    root = root.left
                elif root.right and root.right.val == node:
                    root = root.right
                else:
                    return False
            else:
                return False
        else:
            return True

# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)