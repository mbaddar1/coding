import heapq
from typing import List, Tuple, Any


def heapify_internal(arr: List[Tuple[float, Any]], i):
    n = len(arr)
    l = 2 * i + 1
    r = 2 * i + 2
    # find the largest of the small tree
    lowest = i
    if l < n and arr[l][0] < arr[lowest][0]:
        lowest = l
    if r < n and arr[r][0] < arr[lowest][0]:
        lowest = r
    if lowest != i:
        # this pair of swaps are the core operations
        tmp = arr[i]
        arr[i] = arr[lowest]
        arr[lowest] = tmp
        heapify_internal(arr, lowest)


def heapify2(arr: List[Tuple[float, Any]]):
    n = len(arr)
    start_idx = n // 2 - 1
    for i in range(start_idx, -1, -1):
        heapify_internal(arr, i)


def check_min_heap(a: List[Tuple[float, Any]]) -> bool:
    return check_min_heap_aux(a, 0)


def check_min_heap_aux(a: List[Tuple[float, Any]], i: int) -> bool:
    n = len(a)
    l = 2 * i + 1
    r = 2 * i + 2
    if l < n and a[i][0] > a[l][0]:
        return False
    if r < n and a[i][0] > a[r][0]:
        return False
    if l < n:
        res = check_min_heap_aux(a, l)
        if not res:
            return False
    if r < n:
        return check_min_heap_aux(a, r)
    return True


if __name__ == '__main__':
    a = [(4, None), (10, None), (3, None), (5, None), (1, None)]
    print(check_min_heap(a))
    heapify2(a)
    print(check_min_heap(a))
    #
    # for v in a:
    #     print(v)
    # chk_res = check_min_heap(a)
    # print(chk_res)
