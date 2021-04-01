class Solution {
    public int[][] reconstructQueue(int[][] people) {
        int[][] result = new int[people.length][2];
        for (int[] ints : result) {
            ints[1] = -1;
        }
        Arrays.sort(people, Comparator.comparingInt(o -> o[0]));
        for (int[] person : people) {
            int count = 0;
            for (int i = 0; i < result.length; i++) {
                if (result[i][1] == -1 && count == person[1]) {
                    result[i] = person;
                    break;
                } else if (result[i][1] == -1 || result[i][0] >= person[0]) {
                    count++;
                }
            }
        }
        return result;
    }
}