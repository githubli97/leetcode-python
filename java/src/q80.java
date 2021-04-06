class q80 {
    public int removeDuplicates(int[] nums) {
        if (nums.length <=2) {
            return nums.length;
        }

        int slowIndex = 2;
        int quickIndex = 2;
        for (; quickIndex < nums.length; quickIndex++) {
            if (nums[quickIndex] == nums[slowIndex - 1] && nums[slowIndex - 2] == nums[quickIndex]) {
            } else {
                nums[slowIndex] = nums[quickIndex];
                slowIndex++;
            }
        }
        return slowIndex;
    }
}