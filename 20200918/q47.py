from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        # result = [nums]
        result = []
        for i in range(len(nums)):
            cNums = nums.copy()
            for k in range(i + 1, len(nums)):
                if cNums[i] != cNums[k]:
                    cNums[i] = cNums[i] + cNums[k]
                    cNums[k] = cNums[i] - cNums[k]
                    cNums[i] = cNums[i] - cNums[k]
                    result.append(cNums)
                    cNums = nums.copy()
        return result
if __name__ == '__main__':
    print(Solution().permuteUnique([1, 2, 1]))
    # print(Solution().permuteUnique([1, 2, 3]))