from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dictQueue, result = {}, []

        for s in strs:
            newS = "".join(sorted(list(s)))
            if dictQueue.__contains__(newS):
                dictQueue[newS].append(s)
            else:
                dictQueue[newS] = [s]

        for child in dictQueue.values():
            result.append(child)
        return result

if __name__ == '__main__':
    print(Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))