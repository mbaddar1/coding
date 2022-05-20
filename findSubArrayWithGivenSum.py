"""
https://www.geeksforgeeks.org/find-subarray-with-given-sum-in-array-of-integers/
"""
import numpy as np


def findSubArr(arr, s):
    n = len(arr)
    sum_arr = np.zeros(n)
    sum_arr[0] = arr[0]
    sum_dict = dict()
    for i in range(1, n):
        sum_arr[i] = arr[i] + sum_arr[i - 1]
        if sum_arr[i] == s:
            return 0, i
        if sum_arr[i] - s in sum_dict.keys():
            return sum_dict[sum_arr[i] - s] + 1, i
        sum_dict[int(sum_arr[i])] = i
    return None, None


if __name__ == '__main__':
    arr = [1, 4, 20, 3, 10, 5]
    s = 33
    r = findSubArr(arr, s)
    print(r)

    arr = [0, 2, -2, -20, 10]
    s = -10
    r = findSubArr(arr, s)
    print(r)

    arr = [10, 2, -2, -20, 10]
    s = -10
    r = findSubArr(arr, s)
    print(r)

    arr = [-10, 0, 2, -2, -20, 10]
    s = 20
    r = findSubArr(arr, s)
    print(r)
