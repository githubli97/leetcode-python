import javax.sound.midi.Soundbank;
import java.util.*;

class Solution {
    public List<List<Integer>> permute(int[] nums) {
        List<List<Integer>> ans = new LinkedList<>();
        backtracking(nums, 0, ans);
        return ans;
    }

    public void backtracking(int[] nums, int level, List<List<Integer>> ans) {
        if (level == nums.length - 1) {
            List<Integer> result = new ArrayList<>();
            for (int num : nums) {
                result.add(num);
            }

            ans.add(result);
            return;
        }
        for (int i = level; i < nums.length; i++) {
            int tmp = nums[i];
            nums[i] = nums[level];
            nums[level] = tmp;

            backtracking(nums, level + 1, ans);

            tmp = nums[i];
            nums[i] = nums[level];
            nums[level] = tmp;
        }
    }

    public static void main(String[] args) {
        List<List<Integer>> permute = new Solution().permute(new int[]{1, 2, 3});
        System.out.println(permute);
    }
}