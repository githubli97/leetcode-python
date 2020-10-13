from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict, result = {}, []
        for i in range(len(nums)):
            if target - nums[i] in dict:
                result.append(dict[target - nums[i]])
                result.append(i)
                return result
            else:
                dict[nums[i]] = i
        return result
