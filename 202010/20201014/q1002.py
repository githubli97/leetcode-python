from typing import List


class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        result = []
        for char in A[0]:
            for str in range(1, len(A)):
                for charB in range(len(A[str])):
                    if char == A[str][charB]:
                        A[str] = A[str].replace(char, "", 1)
                        break
                else:
                    break
            else:
                result.append(char)
        return result

if __name__ == '__main__':
    print(Solution().commonChars(["cool","lock","cook"]))