class Solution {
    public void sortColors(int[] nums) {
        int[] count = new int[3];
        for (int num : nums) {
            count[num]++;
        }
        int j = 0;
        for (int i = 0; i < count.length; i++) {
            for (int i1 = 0; i1 < count[i]; i1++) {
                nums[j++] = i;
            }
        }
    }
}