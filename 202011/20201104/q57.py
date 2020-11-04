from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        left, right = newInterval
        result, flag = [], True
        for li, ri in intervals:
            if ri < left:
                result.append([li, ri])
            elif li > right:
                if flag:
                    flag = False
                    result.append([left, right])
                result.append([li, ri])
            else:
                left = min(left, li)
                right = max(ri, right)
        if flag:
            result.append([left, right])

        return result
