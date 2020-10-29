from typing import List


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        arr.sort()
        result, prevNum, count = [], arr[0], 1
        for i in range(1, len(arr)):
            if prevNum == arr[i]:
                count += 1
            else:
                prevNum = arr[i]
                if count in result:
                    return False
                result.append(count)
                count = 1
        return True