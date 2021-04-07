class Solution {
    public int clumsy(int N) {
        int result = 0;
        int tmp = 0;
        for (int j = 0; j < N; j++) {
            int i = N - j;
            if (j % 4 ==0 ) {
                if (j >= 4) {
                    tmp += -1 * i;
                } else {
                    tmp += i;
                }
            }
            if (j % 4 ==1) {
                tmp *= i;
            }
            if (j % 4 ==2) {
                tmp /= i;
                result += tmp;
                tmp = 0;
            }
            if (j % 4 ==3) {
                tmp += i;
                result += tmp;
                tmp = 0;
            }
        }

        return result + tmp;
    }
}