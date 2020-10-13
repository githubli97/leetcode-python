from typing import List


class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        i = 2
        while i < len(arr):
            if arr[i] % 2 == 0:
                i += 3
                continue
            if arr[i - 1] % 2 == 0:
                i += 2
                continue
            if arr[i] % 2 == 0:
                i += 1
                continue
            return True
        return False
