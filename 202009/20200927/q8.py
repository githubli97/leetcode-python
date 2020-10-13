class Solution:
    def myAtoi(self, str: str) -> int:
        result: int = 0
        isNegative = False
        isStart = False
        for c in str:
            if isStart:
                if '0' <= c and '9' >= c:
                    result *= 10
                    result += int(c)
                else:
                   break
            else:
                if '-' == c:
                    isNegative = True
                elif '0' <= c and '9' >= c:
                    result *= 10
                    result += int(c)
                elif ' ' == c:
                    continue
                else:
                    return 0
                isStart = True
        if isNegative:
            result *= -1

        return result



if __name__ == '__main__':
    s = Solution()
    print(s.myAtoi("-91283472332"))