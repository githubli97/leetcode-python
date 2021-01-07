from typing import List


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        result = [[]]
        child = 0
        n = len(isConnected)
        for i in range(n):
            flag = False
            for childArr in result:
                if childArr.__contains__(i):
                    flag = True
            if flag:
                continue

            queue = [i]
            result.append([])
            result[child].append(i)
            while queue:
                node = queue.pop(0)
                for j in range(n):
                    if isConnected[node][j] and j != node and not result[child].__contains__(j):
                        queue.append(j)
                        result[child].append(j)

            child += 1
        return len(result) - 1

if __name__ == '__main__':
    print(Solution().findCircleNum([[1,0,0],[0,1,0],[0,0,1]]))
