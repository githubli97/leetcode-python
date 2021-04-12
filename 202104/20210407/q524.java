import java.util.List;

class Solution {
    public String findLongestWord(String s, List<String> dictionary) {
        char[] chars = s.toCharArray();

        int sLength = s.length();
        int maxIndex = -1;
        int maxLength = 0;
        int k = 0;
        dictionary.sort(String::compareTo);
        for (String s1 : dictionary) {
            int s1Length = s1.length();
            char[] chars1 = s1.toCharArray();
            int j = 0;
            for (int i = 0; i < sLength; i++) {
                if (chars[i] == chars1[j]) {
                    j++;
                }
                if (j == s1Length) {
                    break;
                }
            }
            if (j == s1Length && maxLength < j) {
                maxLength = j;
                maxIndex = k;
            }
            k++;
        }
        return maxIndex == -1? "": dictionary.get(maxIndex);
    }
}