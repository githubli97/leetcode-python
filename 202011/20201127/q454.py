from typing import List


class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        if not A:
            return 0
        def sameNum(arr: List[int]) -> dict:
            result = {}
            for i in arr:
                if i in result:
                    result[i] += 1
                else:
                    result[i] = 1
            return result

        def zeroSubtraction(da: dict, db: dict) -> dict:
            result: dict = {}
            for a in da.keys():
                for b in db.keys():
                    if result.__contains__((a + b)):
                        result[(a + b)] += da[a] * db[b]
                    else:
                        result[(a + b)] = da[a] * db[b]
            return result

        def theEnd(da: dict, db: dict) -> int:
            result = 0
            for a in da.keys():
                if db.__contains__(-a):
                    result += da[a] * db[-a]
            return result



        da = sameNum(A)
        db = sameNum(B)
        dc = sameNum(C)
        dd = sameNum(D)

        d1 = zeroSubtraction(da, db)
        d2 = zeroSubtraction(dc, dd)
        result = theEnd(d1, d2)

        return result





if __name__ == '__main__':
    print(Solution().fourSumCount([-1,-1],[-1,1], [-1,1],[1,-1]))






