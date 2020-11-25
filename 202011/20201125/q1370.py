class Solution:
    def sortString(self, s: str) -> str:
        def reverseSort(s: str, flag: bool) -> (str, bool):
            if not s:
                return "", flag
            tmp = []
            for c in s:
                if c not in tmp:
                    tmp.append(c)
                    s = s.replace(c, "", 1)
            tmp.sort()
            if flag:
                tmp.reverse()
            return "".join(tmp) + reverseSort(s, not flag)[0], not flag
        tmp, reverse = reverseSort(s, False)
        return tmp



if __name__ == '__main__':
    print(Solution().sortString("aaabbbccc"))