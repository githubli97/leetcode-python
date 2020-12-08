import math
from typing import List

class Solution:
    def splitIntoFibonacci(self, S: str) -> List[int]:
        lengthS = math.ceil(len(S) / 3)
        result = []
        copyS = S + ""
        for i in range(1, lengthS + 1):
            for j in range(1, lengthS + 1):
                S = copyS + ""
                a = S[0: i]
                S = S.replace(a, "", 1)
                if S.__contains__('0') and S.index('0') == 0:
                    b = "0"
                else:
                    b = S[0: j]
                S = S.replace(b, "", 1)
                if a != '0' and a.__contains__('0') and a.index('0') == 0:
                    continue
                result.append(int(a))
                result.append(int(b))
                while S:
                    if b != '0' and b.__contains__('0') and b.index('0') == 0:
                        result = []
                        break
                    aAddb = int(a) + int(b)
                    if not S.__contains__(str(aAddb)) or S.index(str(aAddb)) != 0:
                        result = []
                        break
                    if int(aAddb) > pow(2, 31) - 1:
                        return []
                    result.append(int(aAddb))
                    a = b
                    b = str(aAddb)
                    S = S.replace(b, "", 1)
                else:
                    return result
        return result
if __name__ == '__main__':
    print(Solution().splitIntoFibonacci("1101111"))







