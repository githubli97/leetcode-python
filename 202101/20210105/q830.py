from typing import List


class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        result = []
        if not len(s):
            return result
        slow, count, child = 0, 1, [0]
        for fast in range(1, len(s)):
            if s[slow] == s[fast]:
                count += 1
            else:
                if count >= 3:
                    child.append(slow)
                    result.append(child)
                count = 1
                child = [fast]
            slow += 1
        if count >= 3:
            child.append(slow)
            result.append(child)
        return result

if __name__ == '__main__':
    print(Solution().largeGroupPositions("abbxxxxzyyyyyy"))