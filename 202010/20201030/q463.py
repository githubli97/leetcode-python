from typing import List


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    count += 4
                    if i + 1 < len(grid):
                        if grid[i + 1][j] == 1:
                            count -= 1
                    if i - 1 >= 0:
                        if grid[i - 1][j] == 1:
                            count -= 1
                    if j + 1 < len(grid[i]):
                        if grid[i][j + 1] == 1:
                            count -= 1
                    if j - 1 >= 0:
                        if grid[i][j - 1] == 1:
                            count -= 1
        return count
