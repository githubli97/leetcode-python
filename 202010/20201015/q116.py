"""
# Definition for a Node.
"""
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root
        prev, stack = None, [root, None]
        while len(stack) != 1:
            node = stack.pop(0)
            if node:
                if node.left:
                    stack.append(node.left)
                if node.right:
                    stack.append(node.right)
                if prev:
                    prev.next = node
                    prev = node
            else:
                prev = stack[0]
                stack.append(None)
        return root