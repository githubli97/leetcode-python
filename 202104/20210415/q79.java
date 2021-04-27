class Solution {
    public boolean exist(char[][] board, String word) {
        int m = board.length;
        int n = board[0].length;

        for (int i = 0; i < m; i++) {
            for (int i1 = 0; i1 < n; i1++) {
                if (deptSearch(board, word, 0, m, n, i, i1, new int[m][n])) {
                    return true;
                }
            }
        }
        return false;
    }
    public boolean deptSearch(char[][] board, String word, int wordIndex, int m, int n, int mIndex, int nIndex, int[][] used) {
        if (wordIndex == word.length()) {
            return true;
        }
        if (m == mIndex || n == nIndex || mIndex < 0|| nIndex < 0 || used[mIndex][nIndex] == 1) {
            return false;
        }

        if (board[mIndex][nIndex] == word.charAt(wordIndex)) {
            used[mIndex][nIndex] =1;
            wordIndex++;
        } else {
            return false;
        }

        boolean next1 = deptSearch(board, word, wordIndex, m, n, mIndex+1, nIndex, used);
        boolean next2 = deptSearch(board, word, wordIndex, m, n, mIndex-1, nIndex, used);
        boolean next3 = deptSearch(board, word, wordIndex, m, n, mIndex, nIndex+1, used);
        boolean next4 = deptSearch(board, word, wordIndex, m, n, mIndex, nIndex-1, used);
        used[mIndex][nIndex] =0;
        return next1 || next2 || next3 || next4;
    }

    public static void main(String[] args) {
        System.out.println(new Solution().exist(new char[][]{{'A','B','C','E'},{'S','F','C','S'},{'A','D','E','E'}}, "ABCCED"));
    }
}