from typing import List


class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        source = len(stones)
        parents = list(range(source))

        def find(index: int) -> int:
            if parents[index] != index:
                return find(parents[index])
            return index

        def union(node1: int, node2: int):
            parents[find(node1)] = node2

        for i in range(source):
            for j in range(i + 1, source):
                if stones[i][0] == stones[j][0] or stones[i][1] == stones[j][1]:
                    if find(j) != find(i):
                        union(j, i)
        result = set()
        for i in parents:
            result.add(find(i))
        return source - len(result)
if __name__ == '__main__':
    print(Solution().removeStones([[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]))

