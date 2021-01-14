from typing import List


class Solution:
    def pathInZigZagTree(self, label: int) -> List[int]:
        source = label
        result1 = [label]
        while label != 1:
            if label % 2:
                label -= 1
            label = label // 2
            result1.insert(0, label)

        a = 2 ** len(result1) - 1
        b = 2 ** (len(result1) - 1)
        mirror = a - source + b

        result2 = [mirror]
        while mirror != 1:
            if mirror % 2:
                mirror -= 1
            mirror = mirror // 2
            result2.insert(0, mirror)
        result = list()
        for i in range(len(result1)):
            if len(result1) % 2:
                result.append(result1[i] if not i % 2 else result2[i])
            else:
                result.append(result1[i] if i % 2 else result2[i])
        return result
if __name__ == '__main__':
    print(Solution().pathInZigZagTree(1000000))