class q88 {
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        int mergeIndex = nums1.length - 1;
        m -= 1;
        n -= 1;
        while (mergeIndex > -1) {
            if (m < 0) {
                nums1[mergeIndex--] = nums2[n--];
                continue;
            }
            if (n < 0) {
                nums1[mergeIndex--] = nums1[m--];
                continue;
            }

            if (nums1[m] >= nums2[n]) {
                nums1[mergeIndex--] = nums1[m--];
            } else {
                nums1[mergeIndex--] = nums2[n--];
            }
        }
    }
}