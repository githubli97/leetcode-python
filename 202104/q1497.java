class Solution {
    public boolean canArrange(int[] arr, int k) {
        int[] mod = new int[k];
        for (int i : arr) {
            mod[(k+i % k)%k]++;
        }
        for (int i = 1; i < mod.length-i; i++) {
            if (mod[i] != mod[mod.length-i]) {
                return false;
            }
        }
        return mod[0]%2 == 0;
    }
}