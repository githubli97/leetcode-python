from typing import List


class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        result = []
        for i in range(len(nums)):
            count = 0
            for k in range(len(nums)):
                if nums[i] > nums[k]:
                    count += 1
            result.append(count)
        return  result