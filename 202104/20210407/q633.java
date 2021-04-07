class Solution {
    public boolean judgeSquareSum(int c) {
        double pow = Math.pow(c, 0.5);
        int minIndex = 0;
        int target = (int) Math.floor(pow);
        int maxIndex = target;
        while (minIndex <= maxIndex) {
            int sum = (int) (Math.pow(minIndex, 2) + Math.pow(maxIndex, 2));
            if (c == sum) {
                return true;
            } else if (c > sum) {
                minIndex++;
            } else {
                maxIndex--;
            }
        }

        return false;
    }

    public static void main(String[] args) {
        System.out.println(new Solution().judgeSquareSum(5));
    }
}