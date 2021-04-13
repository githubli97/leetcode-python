import java.util.*;

class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        HashMap<Integer, Integer> count = new HashMap<>();
        // int[] count = new int[nums[nums.length -1 ] + 1];
        int max = 0;
        for (int num : nums) {
            if (null == count.get(num)) {
                count.put(num, 0);
            }
            max = Math.max(count.put(num, count.get(nums) + 1) +1, max);
        }
        ArrayList<Integer>[] objects = new ArrayList[max + 1];
        for (Map.Entry<Integer, Integer> integerIntegerEntry : count.entrySet()) {
            if (null == objects[integerIntegerEntry.getValue()]) {
                objects[integerIntegerEntry.getValue()] = new ArrayList<Integer>();
            }
            objects[integerIntegerEntry.getValue()].add(integerIntegerEntry.getKey());
        }
        int[] result = new int[k];
        int j = 0;
        for (int i = objects.length - 1; i >= 0; i--) {
            if (null == objects[i]) {
                continue;
            }
            for (Integer integer : objects[i]) {
                result[j++] = integer;
                if (j == k) {
                    return result;
                }
            }
        }
        return result;
    }
}