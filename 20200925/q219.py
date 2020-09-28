from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dictNums = {}
        for i in range(len(nums)):
            if nums[i] in dictNums and i - dictNums[nums[i]] <= k:
                return True
            dictNums[nums[i]] = i
if __name__ == '__main__':
    s = Solution()
    print(s.containsNearbyDuplicate([1,2,3,1], 3))