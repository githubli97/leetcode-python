from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        majoy = None
        for i in nums:
            if count == 0:
                majoy = i
                count += 1
            else:
                if majoy == i:
                    count += 1
                else:
                    count -= 1

        numCount = 0
        if count > 0:
            for i in nums:
                if i == majoy:
                    numCount += 1
                if numCount > (len(nums)/2):
                    return i
            return -1


if __name__ == '__main__':
    s = Solution()
    print(s.majorityElement([2,3,3,4,4,4]))