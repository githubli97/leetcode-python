class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        while senate:
            i = 0
            while i < len(senate):
                if senate[i] == "R":
                    if senate[i: len(senate)].__contains__("D"):
                        i += 1
                        senate = senate[0: i] + senate[i: len(senate)].replace("D", "", 1)
                    elif senate[0: i].__contains__("D"):
                        senate = senate.replace("D", "", 1)
                    else:
                        return "Radiant"
                else:
                    if senate[i: len(senate)].__contains__("R"):
                        i += 1
                        senate = senate[0: i] + senate[i: len(senate)].replace("R", "", 1)
                    elif senate[0: i].__contains__("R"):
                        senate = senate.replace("R", "", 1)
                    else:
                        return "Dire"

if __name__ == '__main__':
    print(Solution().predictPartyVictory("DRRDRDRDRDDRDRDR"))