from typing import List


class Solution:
    def validMountainArray(self, A: List[int]) -> bool:
        if len(A) < 3:
            return False

        prev, count, up = A[0], True, False
        for i in range(1, len(A)):
            if prev < A[i] and count:
                prev = A[i]
                up = True
            elif prev > A[i] and count:
                count = False
                prev = A[i]
            elif prev > A[i] and not count:
                prev = A[i]
            else:
                return False
        return not count and up