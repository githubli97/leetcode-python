from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                for k in range(j + 1, len(nums)):
                    for l in range(k + 1, len(nums)):
                        if nums[i] + nums[k] + nums[j] + nums[l] == target:
                            result.append([nums[i], nums[j], nums[k], nums[l]])
        return  result

if __name__ == '__main__':
