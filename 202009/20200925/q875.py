import math
from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], H: int) -> int:
        k, maxK = 1, max(piles)
        while k < maxK:
           avg = (maxK + k) // 2
           if sum(math.ceil(p / avg) for p in piles) <= H:
               maxK = avg
           else:
               k = avg + 1
        return k

if __name__ == '__main__':
    print(Solution().minEatingSpeed([2, 2], 2))

