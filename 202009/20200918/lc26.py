from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        nlen = len(nums)
        if 0 == nlen:
            return 0

        k = 0
        for i in range(1, nlen):
            if nums[i] != nums[k]:
                k += 1
            nums[k] = nums[i]

        return k + 1

if __name__ == '__main__':
    nums = [1, 1, 1, 2, 3, 4, 5, 5]
    s = Solution()
    s.removeDuplicates(nums)
    print(nums)