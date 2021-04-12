class Solution {
    public int findMin(int[] nums) {

        int n = nums.length;
        int result = nums[0];
        if (n == 1) {
            return result;
        }
        int l = 0, r = nums.length - 1;
        while (l <= r) {
            int mid =(l + r) / 2;

            if (nums[l] <= nums[mid]) {
                // 前半段有序
                result = Math.min(result, nums[l]);
                l = mid + 1;
            } else {
                // 后半段有序
                result = Math.min(result, nums[mid]);
                r = mid - 1;
            }
        }
        return result;
    }
}