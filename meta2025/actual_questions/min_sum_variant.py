"""
Verbal
Given two array D (Departure-Cost) and R (Return Cost)
Both have length n
return the min (trip cost)
i.e. min sum(D[i]+D[j])
"""
from typing import List


def find_min_travel_distance(D: List[int], R: List[int]) -> float:
    n = len(D)

    min_R = [-1]*n
    min_R[n-1] = R[n-1]
    for i in range(n-2,-1,-1):
        min_R[i] = min(min_R[i+1],R[i])
    tot_min = D[0]+min_R[0]
    for i in range(1,n):
        tot_min = min(tot_min,D[i]+min_R[i])
    return tot_min
if __name__ == "__main__":
    D = [3, 7, 1, 9, 4]
    R = [8, 1, 6, 8, 5]
    r = find_min_travel_distance(D,R)
