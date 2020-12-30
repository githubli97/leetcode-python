from typing import List


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while stones and len(stones) != 1:
            stones.sort()
            a = stones.pop(-1)
            b = stones.pop(-1)
            if a - b:
                stones.append(a - b)
        else:
            if stones:
                return stones[0]
            else:
                return 0