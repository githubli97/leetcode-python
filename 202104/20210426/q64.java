class Solution {
    public int minPathSum(int[][] grid) {
        int m = grid.length;
        int n = grid[0].length;
        for (int i = 0; i < m; i++) {
            for (int i1 = 0; i1 < n; i1++) {
                if (i == 0 && i1 ==0) {
                    continue;
                } else if (i == 0) {
                    grid[i][i1] += grid[i][i1 - 1];
                } else if (i1 == 0) {
                    grid[i][i1] += grid[i - 1][i1];
                } else {
                    grid[i][i1] += Math.min(grid[i][i1 - 1], grid[i - 1][i1]);
                }
            }
        }
        return grid[m - 1][n - 1];
    }
}