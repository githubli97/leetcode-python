from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:

        if len(height) == 0:
            return 0

        maxIndex = 0
        lastIndex = hLen = len(height) - 1
        for i in range(len(height)):
            if height[i] == max(height):
                maxIndex = i
                break
            hLen -= 1

        v = 0
        currHeight = height[0]
        for i in range(1, maxIndex + 1):
            if currHeight > height[i]:
                v += (currHeight - height[i])
            else:
                currHeight = height[i]

        currHeight = height[lastIndex]
        for i in range(maxIndex + 1, len(height)):
            if currHeight > height[lastIndex]:
                v += (currHeight - height[lastIndex])
            else:
                currHeight = height[lastIndex]
            lastIndex -= 1
        return v
if __name__ == '__main__':
    s = Solution()
    print(s.trap([0,1,0,2,1,0,1,3,2,1,2,1]))
    # print(s.trap([0,1,0]))



