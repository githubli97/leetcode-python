from typing import List


class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        windowSize = n - k
        s = sum(cardPoints[:windowSize])
        minSum = s
        for i in range(windowSize, n):
            s += cardPoints[i] - cardPoints[i - windowSize]
            minSum = min(minSum, s)
        return sum(cardPoints) - minSum