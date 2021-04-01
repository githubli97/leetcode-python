class Solution {
    public int minCost(String s, int[] cost) {
        char[] chars = s.toCharArray();
        int result = 0;
        for (int i = 0; i < chars.length-1; i++) {
            if (chars[i] == chars[i+1]) {
                result += Math.min(cost[i], cost[i + 1]);
                cost[i + 1] = Math.max(cost[i], cost[i + 1]);
            }
        }
        return result;
    }
}