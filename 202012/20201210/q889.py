# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def constructFromPrePost(self, pre: List[int], post: List[int]) -> TreeNode:
        if not pre:
            return None
        preFirstNode = pre.pop(0)
        post.pop(-1)
        root = TreeNode(preFirstNode)

        if pre:

            leftChildNode = pre[0]
            leftIndex = post.index(leftChildNode)


            root.left = self.constructFromPrePost(pre[0: leftIndex+1], post[0: leftIndex+1])
            root.right = self.constructFromPrePost(pre[leftIndex+1: len(pre)], post[leftIndex+1: len(pre)])

        return root
