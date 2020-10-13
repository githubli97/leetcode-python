from typing import List


class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        result = []
        i = 0
        k = len(A) - 1
        while i <= k:
            if A[i] < 0:
                A[i] *= -1
            if A[k] < 0:
                A[k] *= -1

            if A[i] > A[k]:
                 result.insert(0, A[i] ** 2)
                 i += 1
            else:
                result.insert(0, A[k] ** 2)
                k -= 1
        return result

if __name__ == '__main__':
    s = Solution()
    A = [-3,-3,-2,1]
    print(s.sortedSquares(A))