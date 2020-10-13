from typing import List


class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        if k <= 0:
            return arr[0]
        elif k < (len(arr) - 1):
            slow = 0
            currentIndex = 0
            i = 1
            while True:
                if arr[currentIndex] > arr[i]:
                    slow += 1
                else:
                    slow = 1
                    currentIndex = i
                if slow == k:
                    return arr[currentIndex]
                if i == (len(arr) - 1):
                    i = 0
                else:
                    i += 1
        else:
            return max(arr)




if __name__ == '__main__':
    arr = [1,25,35,42,68,70]
    k = 2
    s = Solution()
    print(s.getWinner(arr, k))