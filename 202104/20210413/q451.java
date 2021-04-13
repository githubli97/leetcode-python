class Solution {
        public String frequencySort(String s) {
            char[] chars = s.toCharArray();
            int[] count = new int[97 + 25];
            int maxCount = 0;
            for (char aChar : chars) {
                maxCount = Math.max(++count[aChar - '0'], maxCount);
            }

            int[][] countChar = new int[maxCount + 1][97 + 25];
            for (int i = 0; i < count.length; i++) {
                if (count[i] != 0) {
                    for (int i1 = 0; i1 < 97 + 25; i1++) {
                        if (countChar[count[i]][i1] == 0) {
                            countChar[count[i]][i1] = i;
                            break;
                        }
                    }
                }
            }
            StringBuilder result = new StringBuilder();
            for (int i = countChar.length  - 1; i > 0 ; --i) {
                for (int i1 = 0; i1 < countChar[i].length; i1++) {
                    if (countChar[i][i1] == 0) {
                        break;
                    }
                    for (int i2 = 0; i2 < i; i2++) {
                        result.append((char) (countChar[i][i1] + '0'));
                    }
                }
            }
            return result.toString();
        }
    }