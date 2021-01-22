from typing import List


class Solution:
    def addToArrayForm(self, A: List[int], K: int) -> List[int]:
        def re(K: int) -> List:
            result = []
            while 1:
                result.insert(0, K % 10)
                K = K // 10
                if not K:
                    return result


        if not A:
            return re(K)
        index = len(A) - 1
        for i in A:
            K += i * (10 ** index)
            index -= 1
        return re(K)

if __name__ == '__main__':
    print(Solution().addToArrayForm([1,2,0,0], 34))