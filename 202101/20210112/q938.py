class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        if not root:
            return 0
        result = 0
        stack = [root]
        while stack:
            while root.left:
                stack.append(root.left)
                root = root.left
            node = stack.pop(-1)
            if high < node.val:
                return result
            if node.val and low <= node.val:
                result += node.val
            if node.right:
                stack.append(node.right)
                root = node.right
        return result