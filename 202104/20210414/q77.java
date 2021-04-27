import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;

class Solution {
    public List<List<Integer>> combine(int n, int k) {
        List<List<Integer>> ans = new LinkedList<>();
        backtracking(n, k, ans, 1, 0, new int[k]);
        return ans;
    }

    public void backtracking(int n, int k, List<List<Integer>> ans, int pos, int count, int[] child) {
        if (k == count) {
            ArrayList<Integer> list = new ArrayList<>();
            for (int i : child) {
                list.add(i);
            }
            ans.add(list);
            return;
        }

        for (int i = pos; i <= n; i++) {
            child[count++] = i;
            backtracking(n, k, ans, i + 1, count, child);
            count--;
        }
    }

    public static void main(String[] args) {
        System.out.println(new Solution().combine(4,2));
    }
}