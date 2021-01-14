from typing import List


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        length = len(edges)
        parents = list(range(length + 1))
        def find(index: int) -> int:
            if parents[index] != index:
                return find(parents[index])
            return index
        def union(node1: int, node2: int):
            parents[find(node1)] = node2

        for node1, node2 in edges:
            if find(node1) != find(node2):
                union(node1, node2)
            else:
                return [node1, node2]
        return []


if __name__ == '__main__':
    print(Solution().findRedundantConnection([[1,2],[1,3],[2,3]]))