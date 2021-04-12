class Solution {
    public int singleNonDuplicate(int[] nums) {
        int n = nums.length;
        if (n == 1) {
            return nums[0];
        }
        int l = 0, r = n - 1;
        while (l < r) {
            int mid = (l + r) / 2;
            if (nums[mid] == nums[mid + 1]) {
                if (mid % 2 == 0) {
                    l = mid + 2;
                } else {
                    r = mid - 1;
                }
            } else if (nums[mid] == nums[mid - 1]) {
                if ((mid - 1) % 2 == 0) {
                    l = mid + 1;
                } else {
                    r = mid - 2;
                }

            } else {
                return nums[mid];
            }
        }
        return nums[l];
    }
}