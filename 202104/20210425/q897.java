import java.util.LinkedList;

// *
//   Definition for a binary tree node.
class TreeNode {
  int val;
  TreeNode left;
  TreeNode right;
  TreeNode() {}
  TreeNode(int val) { this.val = val; }
  TreeNode(int val, TreeNode left, TreeNode right) {
      this.val = val;
      this.left = left;
      this.right = right;
  }
}
class Solution {
    public TreeNode increasingBST(TreeNode root) {
        if (root == null) {
            return null;
        }
        TreeNode pre = null, ans = null;
        LinkedList<TreeNode> stack = new LinkedList<>();
        stack.add(root);
        while (!stack.isEmpty()) {
            while (null != root.left) {
                stack.addFirst(root.left);
                TreeNode tmp = root;
                root = root.left;
                tmp.left = null;
            }

            TreeNode remove = stack.pop();

            if (pre == null) {
                pre = remove;
                ans = pre;
            } else {
                pre.right = remove;
                pre = pre.right;
            }

            if (remove.right != null) {
                root = remove.right;
                stack.addFirst(root);
            }
        }
        return ans;
    }
}