class Solution {
    public int rob(int[] nums) {
        if (nums.length == 1) {
            return nums[0];
        }
        if (nums.length == 2) {
            return Math.max(nums[0], nums[1]);
        }
        int prev1 = nums[0], prev2 = Math.max(nums[0], nums[1]);
        for (int i = 2; i < nums.length; i++) {
            int tmp = prev2;
            prev2 = Math.max(prev1 + nums[i], prev2);
            prev1 = tmp;
        }
        return prev2;
    }
}