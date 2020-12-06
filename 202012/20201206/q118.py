from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if not numRows:
            return []
        result = [[1], [1, 1]]
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return result

        for i in range(2, numRows):

           prev = result[i - 1]
           child = [1]
           for j in range(1, len(prev)):
               child.append(prev[j] + prev[j - 1])

           child.append(1)
           result.append(child)
        return result
