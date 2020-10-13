class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        hLen, nLen = len(haystack), len(needle)
        if nLen == 0:
            return 0
        if hLen == 0:
            return -1

        i = 0
        while i <= hLen - nLen:
            k = 0
            while k < nLen:
                if haystack[i + k] != needle[k]:
                    break
                k += 1
            if k == nLen:
                return i
            i += 1
        return -1

if __name__ == '__main__':
    s = Solution()
    print(s.strStr("a", "a"))