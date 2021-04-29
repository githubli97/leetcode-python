class Solution {
    public int[][] updateMatrix(int[][] mat) {
        int m = mat.length;
        int n = mat[0].length;
        int[] ans = new int[m];
        for (int i = 0; i < m; i++) {
            ans[i] = m + n;
        }

        for (int i = 0; i < m; i++) {
            for (int i1 = 0; i1 < n; i1++) {
                if (mat[i][i1] == 0) {
                    ans[i][i1] = 0;
                } else if (i == 0 && i1 == 0) {
                    continue;
                } else if (i == 0) {
                    ans[i][i1] = ans[i - 1][i1 - 1] + 1;
                } else if (i1 == 0) {
                    ans[i][i1] = ans[i - 1][i1] + 1;
                } else {
                    ans[i][i1] = Math.min(ans[i - 1][i1], ans[i][i1 - 1]) + 1;
                }
             }
        }
        for (int i = m -1; i > -1; i--) {
            for (int i1 = n - 1; i1 > -1; i1--) {
                if (mat[i][i1] == 0) {
                    ans[i][i1] = 0;
                } else if (i == m - 1 && i1 == n - 1) {
                    continue;
                } else if (i == m - 1) {
                    ans[i][i1] = Math.min(ans[i][i1], ans[i][i1 + 1] + 1);
                } else if (i1 == n - 1) {
                    ans[i][i1] = Math.min(ans[i][i1], ans[i + 1][i1] + 1);
                } else {
                    int minTmp = Math.min(ans[i + 1][i1], ans[i][i1 + 1]) + 1;
                    ans[i][i1] = Math.min(minTmp, ans[i][i1]);
                }
             }
        }
        return ans;
    }
}