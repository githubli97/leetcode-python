from typing import List
class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        if not bills:
            return True

        mine = []
        for i in bills:
            if not mine and i != 5:
                return False
            elif i == 5:
                mine.append(5)
            elif mine and i == 10:
                if mine.__contains__(5):
                    mine.remove(5)
                    mine.append(10)
                else:
                    return False
            elif mine and i == 20:
                if mine.__contains__(10):
                    mine.remove(10)
                    if mine.__contains__(5):
                        mine.remove(5)
                    else:
                        return False
                elif mine.__contains__(5):
                    mine.remove(5)
                    if mine.__contains__(5):
                        mine.remove(5)
                        if mine.__contains__(5):
                            mine.remove(5)
                        else:
                            return False
                    else:
                        return False
                else:
                    return False
        return True

if __name__ == '__main__':
    print(Solution().lemonadeChange([5,5,5,10,5,5,10,20,20,20]))
