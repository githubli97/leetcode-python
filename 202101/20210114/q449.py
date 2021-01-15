class Codec:
    def serialize(self, root: TreeNode) -> str:
        if not root:
            return ""
        stack = [root]
        result = []
        while stack:
            node = stack.pop(-1)
            result.append(str(node.val))
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        print(result)
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
            if int(preorder[k]) > root.val:
                i = k
                break
        root.left = self.deserialize(",".join(preorder[1: i]))
        root.right = self.deserialize(",".join(preorder[i:]))
        return root