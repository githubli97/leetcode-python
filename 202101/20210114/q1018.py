from typing import List


class Solution:
    def prefixesDivBy5(self, A: List[int]) -> List[bool]:
        currentNum = 0
        result = []
        for i in A:
            currentNum *= 2
            currentNum += i
            currentNum %= 5
            if not currentNum:
                result.append(True)
            else:
                result.append(False)
        return result
