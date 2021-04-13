import java.util.HashSet;
import java.util.LinkedList;
import java.util.List;

class Solution {
    public List<List<Integer>> pacificAtlantic(int[][] heights) {
        int width = heights.length;
        int height = heights[0].length;

        List<List<Integer>> result = new LinkedList<>();
        for (int i = 0; i < width; i++) {
            for (int i1 = 0; i1 < height; i1++) {
                if (pacificAtlantic(heights, i, i1)) {
                    LinkedList<Integer> resultChild = new LinkedList<>();
                    resultChild.add(i);
                    resultChild.add(i1);
                    result.add(resultChild);
                }
            }
        }
        return result;
    }

    public boolean pacificAtlantic(int[][] heights, int width, int height) {
        boolean canToLeft = false;
        boolean canToRight = false;

        HashSet<Integer> pass = new HashSet<>();
        LinkedList<int[]> stack = new LinkedList<>();

        stack.add(new int[]{width, height});
        pass.add(width * heights[0].length + height);

        while (!stack.isEmpty()) {
            int[] remove = stack.remove();
            if (remove[0] == 0) {
                canToLeft = true;
            }
            if (remove[1] == 0) {
                canToLeft = true;
            }
            if (remove[0] == heights.length - 1) {
                canToRight = true;
            }
            if (remove[1] == heights[0].length - 1) {
                canToRight = true;
            }
            if (canToLeft && canToRight) {
                return true;
            }

            checkIndex(remove[0] - 1, remove[1], heights, heights[remove[0]][remove[1]], stack, pass);
            checkIndex(remove[0] + 1, remove[1], heights, heights[remove[0]][remove[1]], stack, pass);
            checkIndex(remove[0], remove[1] + 1, heights, heights[remove[0]][remove[1]], stack, pass);
            checkIndex(remove[0], remove[1] - 1, heights, heights[remove[0]][remove[1]], stack, pass);
        }
        return false;
    }

    public void checkIndex(int width, int height, int[][] grid, int currentNumber, LinkedList<int[]> stack, HashSet<Integer> pass) {
        if (width >= 0 && width < grid.length && height >= 0 && height < grid[0].length && grid[width][height] <= currentNumber) {
            if (!pass.contains(width * grid[0].length + height)) {
                stack.add(0, new int[]{width, height});
                pass.add(width * grid[0].length + height);
            }
        }
    }

    public static void main(String[] args) {
        System.out.println(new Solution().pacificAtlantic(new int[][]{{1,2,2,3,5},{3,2,3,4,4},{2,4,5,3,1},{6,7,1,4,5},{5,1,1,2,4}}));
    }
}