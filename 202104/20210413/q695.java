import java.util.LinkedList;

class Solution {
    public int maxAreaOfIsland(int[][] grid) {
        int width = grid.length;
        int height = grid[0].length;
        int maxArea = 0;

        for (int i = 0; i < width; i++) {
            for (int i1 = 0; i1 < height; i1++) {
                if (grid[i][i1] == 1) {
                    maxArea = Math.max(maxArea, maxAreaOfIsland(grid, i, i1));
                }
            }
        }
        return maxArea;
    }
    public int maxAreaOfIsland(int[][] grid, int width, int height) {
        int currLand = 0;
        LinkedList<int[]> land = new LinkedList<>();
        land.add(new int[]{width, height});
        grid[width][height] = 0;
        while (!land.isEmpty()) {
            int[] pop = land.pop();
            currLand++;

            if (checkIndex(pop[0] - 1, pop[1], grid)) {
                land.add(0, new int[]{pop[0] - 1, pop[1]});
            }
            if (checkIndex(pop[0] +1, pop[1], grid)) {
                land.add(0, new int[]{pop[0] +1, pop[1]});
            }
            if (checkIndex(pop[0], pop[1] - 1, grid)) {
                land.add(0, new int[]{pop[0], pop[1] -1});
            }
            if (checkIndex(pop[0], pop[1] + 1, grid)) {
                land.add(0, new int[]{pop[0], pop[1]+ 1});
            }

        }
        return currLand;
    }
    public boolean checkIndex(int width, int height, int[][] grid) {
        if (width >= 0 && width < grid.length && height >= 0 && height < grid[0].length && grid[width][height] == 1) {
            grid[width][height] = 0;
            return true;
        }
        return false;
    }

    public static void main(String[] args) {
        System.out.println(new Solution().maxAreaOfIsland(new int[][]{{1,1,0,0,0},{1,1,0,0,0},{0,0,0,1,1},{0,0,0,1,1}}));
    }
}