from typing import List


def twoSum(arr: List[int], target: int):
    arr_sorted = sorted(arr)
    N = len(arr_sorted)
    i = 0
    j = N - 1
    while i < j:
        if arr[i] + arr[j] == target:
            return i, j
        elif arr[i] + arr[j] < target:
            i = i + 1
        else:
            j = j - 1
    return -1, -1


if __name__ == "__main__":
    r = twoSum([2, 7, 11, 15], 9)
    assert r == (0, 1)

    r = twoSum([2, 6, 11, 15], 9)
    assert r == (-1, -1)

