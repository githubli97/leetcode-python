class Solution {
    public int jump(int[] nums) {
        int n = nums.length;
        int[] dp = new int[n];
        
        for (int i = 0; i < nums.length; i++) {
            for (int i1 = i + 1; i1 < nums.length && i1 <= i + nums[i]; i1++) {
                if (dp[i1] == 0) {
                    dp[i1] = dp[i] + 1;
                }
            }
        }
        for (int i = 1; i < dp.length; i++) {
            if (i == 0) {
                return false;
            }
        }
        return true;
    }

    public static void main(String[] args) {
        System.out.println(new Solution().jump(new int{3,2,1,0,4}));
    }
}