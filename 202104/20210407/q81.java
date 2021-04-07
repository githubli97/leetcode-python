class Solution {
    public boolean search(int[] nums, int target) {
        if (nums.length == 0) {
            return false;
        }
        if (nums.length == 1) {
            return nums[0] == target;
        }
        int l = 0, r = nums.length - 1;
        while (l <= r) {
            int avg = (l + r) / 2;
            if (nums[avg] == target) {
                return true;
            }
            if (nums[l] == nums[r] && target == nums[l]) {
                return true;
            } else if (nums[l] == nums[r]) {
                r = r - 1;
                l = l + 1;
            } else if (nums[l] <= nums[avg]) {
                if (nums[l] <= target && target < nums[avg]) {
                    r = avg - 1;
                } else {
                    l = avg + 1;
                }
            } else {
                if (nums[avg] < target && target <= nums[r]) {
                    l = avg + 1;
                } else {
                    r = avg - 1;
                }
            }
        }
        return false;
    }
}