from typing import List


class Solution:
    def transpose(self, A: List[List[int]]) -> List[List[int]]:
        result = []
        for i in range(len(A[0])):
            aResult = []
            for k in range(len(A)):
                aResult.append(A[k][i])
            result.append(aResult)
        return result

if __name__ == '__main__':
    a = [[1,2,3],[4,5,6]]
    s = Solution()
    print(s.transpose(a))



