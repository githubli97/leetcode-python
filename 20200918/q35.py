from typing import List


# class Solution:
#     def searchInsert(self, nums: List[int], target: int) -> int:
#         for i in range(len(nums)):
#             if nums[i] >= target:
#                 return i
#             elif nums[len(nums) - 1 - i] < target:
#                 return len(nums) - i
#             elif nums[len(nums) - 1 - i] == target:
#                 return len(nums) - i - 1
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)
        while left < right:
            mid = (left + right)//2
            if nums[mid] >= target:
                right = mid
            else:
                left = mid + 1
        return left


if __name__ == '__main__':
    nums = [1, 2, 3, 4, 5]
    s = Solution()
    print(s.searchInsert(nums, 5))
