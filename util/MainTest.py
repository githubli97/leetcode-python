from typing import List


def sameNum(arr: List[int]) -> dict:
    result = {}
    for i in arr:
        if i in result:
            result[i] += 1
        else:
            result[i] = 1
    return result

if __name__ == '__main__':
    # 字符串对比
    str1 = "ab"
    str2 = "abc"
    print(str1[0: 0] == str2[0: 0])


    arr = [1, 2, 3]
    arr.sort()
    sorted(arr)

    print(sameNum([1, 2,3,3,4,5,5,5,5,5]))