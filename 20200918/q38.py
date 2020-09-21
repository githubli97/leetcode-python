class Solution:
    def countAndSay(self, n: int) -> str:
        result = "1"
        for i in range(n - 1):
            count = 1
            preNum = ""
            tResult = ""
            for k in range(len(result)):
                ch = result[k]
                if "" == preNum:
                    preNum = ch
                elif preNum == ch:
                    count += 1
                else:
                    tResult += str(count)
                    tResult += preNum
                    preNum = ch
                    count = 1
            tResult += str(count)
            tResult += preNum

            result = tResult
        return result
if __name__ == '__main__':
    s = Solution()
    print(s.countAndSay(30))
    # result = ""
    # result.__add__("1")
    # result.__add__("2")
    # print(result)