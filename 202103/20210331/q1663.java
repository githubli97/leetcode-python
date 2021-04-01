class Solution {
    public String getSmallestString(int n, int k) {
        k -= n;
        char[] arr = new char[n];
        for (int i = arr.length - 1; i >=0; i--) {
            arr[i] = 97;
            if (k >= 25) {
                arr[i] += 25;
                k -= 25;
            } else {
                arr[i] += k;
                k -= k;
            }
        }

        StringBuilder result = new StringBuilder();
        for (char c : arr) {
            result.append(c);
        }
        return result.toString();
    }
}