from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]
        def findFirst(nums: List[int], target: int, left: int, right: int) -> int:
            avg = (left + right) // 2
            if nums[avg] == target:
                if avg - 1 >= 0 and nums[avg - 1] == target:
                    return findFirst(nums, target, left, avg)
                else:
                    return avg
            elif abs(left - right) <= 1:
                return -1
            elif nums[avg] > target:
                return findFirst(nums, target, left, avg)
            else:
                return findFirst(nums, target, avg, right)
        def findLast(nums: List[int], target: int, left: int, right: int) -> int:
            avg = (left + right) // 2
            if nums[avg] == target:
                if avg + 1 < len(nums) and nums[avg + 1] == target:
                    return findLast(nums, target, avg, right)
                else:
                    return avg
            elif abs(left - right) <= 1:
                return -1
            elif nums[avg] > target:
                return findLast(nums, target, left, avg)
            else:
                return findLast(nums, target, avg, right)
        return [findFirst(nums, target, 0, len(nums)), findLast(nums, target, 0, len(nums))]



if __name__ == '__main__':
    arr = [5,7,7,8,8,10]
    print(Solution().searchRange(arr, 6))
