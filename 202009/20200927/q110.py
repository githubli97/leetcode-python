# class Solution:
#     def isBalanced(self, root: TreeNode) -> bool:
#         def maxDeptByLeaf(root: TreeNode) -> int:
#             leftHigh = rightHigh = 1
#             if not root.left and not root.right:
#                 return 1
#             if root.left:
#                 leftHigh = maxDeptByLeaf(root.left) + 1
#             if root.right:
#                 rightHigh = maxDeptByLeaf(root.right) + 1
#             return max(leftHigh, rightHigh)
#
#         if root:
#             return False
#
#         if abs(minDeptByLeaf(root.left) - minDeptByLeaf(root.right)) > 1:
#             return False
#         return True