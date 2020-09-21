from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if len(nums) == 0:
            return 0
        k = 0
        for i in range(0, len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k



if __name__ == '__main__':
    # nums = [3,2,2,1,3]
    nums = [1, 1, 1, 2, 3, 4, 5, 5]
    s = Solution()
    print(s.removeElement(nums, 1))
    print(nums)