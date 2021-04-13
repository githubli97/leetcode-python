import java.util.LinkedList;

// Definition for a binary tree node.
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
    public int minDiffInBST(TreeNode root) {
        LinkedList<TreeNode> list = new LinkedList<>();
        TreeNode pre = null;
        int result = (int) Math.pow(10, 6);
        while (null != root || !list.isEmpty()) {
            while (null != root) {
                list.add(0, root);
                root = root.left;
            }
            TreeNode pop = list.pop();
            if (null == pre) {
                pre = pop;
            } else {
                result = Math.min(result, pop.val - pre.val);
                pre = pop;
            }
            if (null != pop.right) {
                root = pop.right;
            }
        }
        return result;
    }
}