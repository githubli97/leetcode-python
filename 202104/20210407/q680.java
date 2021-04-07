class Solution {
    public boolean validPalindrome(String s) {

        char[] chars = s.toCharArray();
        int minIndex = 0;
        int maxIndex = chars.length - 1;
        while (minIndex <= maxIndex) {
            if (chars[minIndex] != chars[maxIndex]) {
                return validPalindrome(chars, minIndex + 1, maxIndex) || validPalindrome(chars, minIndex, maxIndex - 1) ;
            }
            minIndex++;
            maxIndex--;
        }
        return true;
    }

    boolean validPalindrome(char[] chars, int minIndex, int maxIndex) {
        while (minIndex <= maxIndex) {
            if (chars[minIndex] != chars[maxIndex]) {
                return false;
            }
            minIndex++;
            maxIndex--;
        }
        return true;
    }
}