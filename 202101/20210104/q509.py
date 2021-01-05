class Solution:
    def fib(self, n: int) -> int:
        result = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711, 28657, 46368, 75025, 121393, 196418, 317811, 514229, 832040]
        return result[n]


if __name__ == '__main__':
    a, b = 1, 1
    result = [1, 1]

    for i in range(2, 30):
        a, b = b, a + b
        result.append(b)
    print(len(result))
    print(result)