class Solution {
    public int numberOfArithmeticSlices(int[] nums) {
        int sum = 0, prev = 0;
        for (int i = 2; i < nums.length; i++) {
            if (nums[i] - nums[i - 1] == nums[i - 1] - nums[i - 2]) {
                prev += 1;
                sum += prev;
            } else {
                prev = 0;
            }
        }
        return sum;
    }
}