# https://leetcode.com/problems/median-of-two-sorted-arrays/
from typing import List

import numpy as np


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n1 = len(nums1)
        n2 = len(nums2)
        N = n1 + n2
        even = True if N % 2 == 0 else False
        med_idx_odd = int((N - 1) / 2)
        med_idx_even = [int((N / 2) - 1), int(N / 2)]
        i = 0
        comb_idx = (0, 0) if nums1[0] < nums2[0] else (1, 0)
        i1 = 0
        i2 = 0
        median_even = [None, None]
        n1_finished = False
        n2_finished = False
        while True:
            if even:
                if i == med_idx_even[0]:
                    median_even[0] = nums1[comb_idx[1]] if comb_idx[0] == 0 else nums2[comb_idx[1]]
                else:
                    median_even[1] = nums1[comb_idx[1]] if comb_idx[0] == 0 else nums2[comb_idx[1]]
                    m = (median_even[0] + median_even[1]) / 2
                    return m
            else:  # odd
                if i == med_idx_odd:
                    m = nums1[comb_idx[1]] if comb_idx[0] == 0 else nums2[comb_idx[1]]
                    return m
            if n1_finished:
                comb_idx = (1, i2)
                i2 = i2 + 1
                i = i + 1

                continue
            if n2_finished:
                comb_idx = (0, i1)
                i1 = i1 + 1
                i = i + 1

                continue
            if comb_idx[0] == 0:
                if i1 < n1 - 1:
                    if nums1[i1 + 1] < nums2[i2]:
                        comb_idx = (0, i1 + 1)
                    else:
                        comb_idx = (1, i2)
                    i1 = i1 + 1
                else:
                    comb_idx = (1, i2)
                    i2 = i2 + 1
                    n1_finished = True
            else:
                if i2 < n2 - 1:
                    if nums2[i2 + 1] < nums1[i1]:

                        comb_idx = (1, i2 + 1)
                    else:
                        comb_idx = (0, i1)
                    i2 = i2 + 1
                else:
                    comb_idx = (0, i1)
                    i1 = i1 + 1
                    n2_finished = True
            i = i + 1


if __name__ == '__main__':
    # num1 = [0, 1]
    # num2 = [2, 3, 4, 5, 6]

    # num1 = [2, 3, 4, 5, 6]
    # num2 = [0, 1]
    nums1 = [0, 2, 4]
    nums2 = [1, 3]
    s = Solution()
    r = s.findMedianSortedArrays(nums1, nums2)
    print(r)
    # num1 = [0, 2, 4]
    # num2 = [1, 3]
    # r = s.findMedianSortedArrays(num1, num2)
    # print(r)
