# 待优化
# Definition for a binary tree node.

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root: TreeNode) -> str:
        if not root:
            return None
        stack = [root]
        result = []
        while stack:
            node = stack.pop(0)
            result.append(str(node.val))
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return ",".join(result)

    def deserialize(self, data: str) -> TreeNode:
        if not data:
            return None
        preorder = data.split(",")
        root = TreeNode(int(preorder[0]))
        if len(preorder) == 1:
            return root
        i = len(preorder)
        for k in range(1, len(preorder)):
            if preorder[k] > root.val:
                i = k
                break
        root.left = self.deserialize(preorder[1: i])
        root.right = self.deserialize(preorder[i:])
        return root

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans

if __name__ == '__main__':
    print("abc,bcd".split(","))
    print("abcbcd".split(","))