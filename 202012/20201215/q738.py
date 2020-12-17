class Solution:
    def monotoneIncreasingDigits(self, N: int) -> int:
        flag, prevNum, copyN, count = True, None, 0, 0
        while N:
            cur = N % 10
            N = N // 10
            count += 1

            if not prevNum and prevNum != 0:
                prevNum = cur
                copyN += copyN * 10 + cur
            elif prevNum < cur:
                flag = False
                prevNum = cur
                copyN += copyN * 10 + cur
                N = N * pow(10, count - 1)
            else:
                prevNum = cur
                copyN += copyN * 10 + cur

        if flag:
            return copyN
        else:
            return prevNum * pow(10, count - 1) - 1

if __name__ == '__main__':
    print(Solution().monotoneIncreasingDigits(12332))