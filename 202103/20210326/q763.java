class Solution {
    public List<Integer> partitionLabels(String S) {
        HashMap<Character, int[]> count = new HashMap<>();
        for (char c : S.toCharArray()) {
            count.put(c, new int[]{S.indexOf(c), S.lastIndexOf(c)});
        }
        ArrayList<int[]> ints = new ArrayList<>(count.values());
        Collections.sort(ints, Comparator.comparingInt(o -> o[0]));

        List<Integer> result = new LinkedList<>();
        int pre = ints.get(0)[1];
        for (int i = 1; i < ints.size(); i++) {
            if (pre > ints.get(i)[0]) {
                pre = Math.max(pre, ints.get(i)[1]);
            } else {
                result.add(pre);
                pre = ints.get(i)[1];
            }
        }
        result.add(S.length());
        for (int i = result.size() - 1; i > 0 ; i--) {
            result.set(i, result.get(i) - result.get(i - 1));
        }
        result.set(0, result.get(0) + 1);
        result.set(result.size() - 1, result.get(result.size() - 1) - 1);
        return result;
    }
}