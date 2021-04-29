class Solution {
    public int maximalSquare(char[][] matrix) {
        int m = matrix.length;
        int n = matrix[0].length;

        int[][] dp = new int[m][n];

        int maxSide = 0;
        for (int i = 0; i < m; i++) {
            for (int i1 = 0; i1 < n; i1++) {
                if (matrix[i][i1] == 48) {
                    continue;
                } else if (i == 0 || i1 == 0) {
                    dp[i][i1] = 1;
                } else {
                    dp[i][i1] = Math.min(Math.min(dp[i - 1][i1], dp[i][i1 - 1]), dp[i - 1][i1 - 1]) + 1;
                }
                maxSide = Math.max(maxSide, dp[i][i1]);
            }
        }
        return maxSide * maxSide;
    }
}