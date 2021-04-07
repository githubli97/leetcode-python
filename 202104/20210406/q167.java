class q167 {
    public int[] twoSum(int[] numbers, int target) {
        int minIndex = 0;
        int maxIndex = numbers.length - 1;
        while (minIndex < maxIndex) {
            if (numbers[minIndex] + numbers[maxIndex] == target) {
                return new int[]{minIndex + 1, maxIndex + 1};
            } else if (numbers[minIndex] + numbers[maxIndex] < target) {
                minIndex++;
            } else {
                maxIndex--;
            }
        }
        return null;
    }
}