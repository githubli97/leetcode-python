from typing import List


class Solution:
    def matrixScore(self, A: List[List[int]]) -> int:
        if not A:
            return 0

        for child in A:
            if not child[0]:
                for i in range(len(child)):
                    child[i] = 0 if child[i] else 1

        lengthA = len(A)

        for i in range(len(A[0])):
            count = 0
            for j in range(lengthA):
                if not A[j][i]:
                    count += 1
            if count > lengthA/2:
                for j in range(lengthA):
                    A[j][i] = 0 if A[j][i] else 1
        result = 0
        for i in range(lengthA):
            count = len(A[0])
            while count > 0:
                if A[i][len(A[0]) - count]:
                    result += pow(2, count - 1)
                count -= 1
        return result

if __name__ == '__main__':
    A = [[0,0,1,1],[1,0,1,0],[1,1,0,0]]

    print(Solution().matrixScore(A))
