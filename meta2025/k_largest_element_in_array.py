# https://leetcode.com/problems/kth-largest-element-in-an-array/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days
from typing import List


def index_sort(nums: List[int]) -> List[int]:
    n = len(nums)
    max_int = max(nums)  # O(n)
    min_int = min(nums)  # O(n)
    counts = [0] * (max_int - min_int + 1)
    for i in range(n):  # O(n)
        idx = nums[i] - min_int
        counts[idx] += 1
    # get sorted array
    sorted_arr = []
    for i in range(len(counts)):
        for j in range(counts[i]):
            v = i + min_int
            sorted_arr.append(v)
    return sorted_arr


def insert_num(num: int, subarr: List[int]) -> None:
    # assume sub_arr is sorted
    if num < subarr[0]:
        return
    # look for insertion index
    j = len(subarr) - 1
    while j >= 0:
        if num < subarr[j]:
            j = j - 1
        else:
            break
    # insert at j and shift till overwriting element at j=0
    for k in range(j):
        subarr[k] = subarr[k + 1]

    subarr[j] = num


def get_kth_top_element(nums: List[int], k: int) -> int:
    n = len(nums)
    if k >= n:
        sorted_arr = sorted(nums)
        return sorted_arr[0]
    else:
        top_k_arr = sorted(nums[:k])  # klogk - init
        for i in range(k, n):
            insert_num(nums[i], top_k_arr)
    return top_k_arr[0]


if __name__ == "__main__":
    # test heapq
    # arr = [12, -7, 0, 25, -3, 9, -15, 4, 18, -1]
    # r = index_sort(arr)
    # print(r)
    # a  = [5,5,8,10,20]
    # print(a)
    # insert_num(9,a)
    # print(a)

    # a = [3,2,1,5,6,4]
    # k = 2
    # r = get_kth_top_element(a, k)
    # print(r)

    nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
    k = 4
    r = get_kth_top_element(nums, k)
    print(r)
