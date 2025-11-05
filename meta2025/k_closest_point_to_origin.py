# https://leetcode.com/problems/k-closest-points-to-origin/description/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days
# DONE Accepted
#   https://leetcode.com/problems/k-closest-points-to-origin/submissions/1821571197
from typing import List

import numpy as np

from meta2025.myHeap import build_heap2, heapify2_index


def get_euclidean_distance(x: List[int]):
    x1 = x[0]
    x2 = x[1]
    return np.sqrt(x1 ** 2 + x2 ** 2)



class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        n = len(points)
        closet_heap = []
        for i in range(k):
            distance = get_euclidean_distance(points[i])
            closet_heap.append((-distance, points[i]))
        build_heap2(closet_heap)
        for i in range(k,n):
            distance = get_euclidean_distance(points[i])
            max_distance_so_far = -closet_heap[0][0]
            if distance <= max_distance_so_far: # <= and <
                closet_heap[0] = (-distance,points[i])
                heapify2_index(closet_heap,0)
        return_list = []
        for e in closet_heap:
            return_list.append(e[1])
        return return_list


if __name__ == "__main__":
    # points = [[3,3],[5,-1],[-2,4]]
    s = Solution()
    # r = s.kClosest(points, 2)
    # print(r)
    # ex1
    k = 3
    points = [(1,2), (-2,1), (3,4), (-1,-1), (0,0), (2,-2), (5,0), (-3,3), (1,-3), (2,1), (-4,-1), (0,5), (4,-4), (-2,-3), (3,0), (-1,4), (2,2), (-5,2), (0,-4), (1,0)]
    r = s.kClosest(points,k)
    print(r)
    # ex2
    points = [(7,1), (-6,2), (5,-5), (4,3), (-1,-4), (2,2), (-3,0), (0,6), (3,-1), (-2,-2), (6,6), (-5,-5), (1,1), (0,-7), (4,-2), (-4,4), (2,-3), (-1,5), (5,0), (0,0)]
    k = 5
    r = s.kClosest(points,k)
    print(r)
    # ex3
    points = [(10,0), (0,10), (-10,0), (0,-10),(3,4), (-3,4), (3,-4), (-3,-4),(1,0), (0,1), (-1,0), (0,-1),(2,2), (-2,2), (2,-2), (-2,-2),(5,12), (-5,12), (8,6), (-8,6)]
    k = 8
    r = s.kClosest(points,k)
    print(r)



