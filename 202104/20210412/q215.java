class Solution {
    public int findKthLargest(int[] nums, int k) {
        return findKthLargest(nums, 0, nums.length, k);
    }
    public int findKthLargest(int[] nums, int l, int r, int k) {
        if (r - l <= 1) {
            return nums[l];
        }

        int frist = l, last = r - 1, key = nums[frist];
        while (frist < last) {
            while (frist < last && key >= nums[last]) {
                last--;
            }
            nums[frist] = nums[last];
            while (frist < last && key <= nums[frist]) {
                frist++;
            }
            nums[last] = nums[frist];
        }
        nums[frist] = key;
        if (frist == k - 1) {
            return key;
        } else if (frist > k - 1) {
            return findKthLargest(nums, l, frist, k);
        } else {
            return findKthLargest(nums, frist + 1, r, k);
        }
    }

    public static void main(String[] args) {
        System.out.println(new Solution().findKthLargest(new int[]{3, 2, 1, 5, 6, 4}, 2));
    }
}