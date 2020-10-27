class Solution:
    def numTrees(self, n: int) -> int:
        stack = [1, 1]
        for i in range(2, n + 1):
            count = 0
            for k in range(i):
                count += stack[k - 0] * stack[i - 1 - k]
            stack.append(count)
        return stack[n]