
class Solution {
    public boolean checkPossibility(int[] nums) {
        if (nums.length == 1) {
            return true;
        }
        boolean flag = nums[0] <= nums[1];
        for (int i = 1; i < nums.length-1; i++) {
            if (nums[i] > nums[i+1]) {
                if (!flag) {
                    return false;
                }
                if (nums[i + 1] >= nums[i - 1]) {
                    nums[i] = nums[i + 1];
                } else {
                    nums[i+ 1] = nums[i];
                }
                flag = false;
            }
        }
        return true;
    }
}