"""
https://leetcode.com/problems/partition-equal-subset-sum/
"""
# TODO test cases
from typing import List
import numpy as np


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        tot_Sum = sum(nums)
        n = len(nums)
        if n == 0:
            return False
        if tot_Sum % 2 != 0:
            return False
        subSum = int(tot_Sum / 2)
        dp_arr = np.full(shape=(n, subSum + 1), fill_value=False)
        dp_arr[0][0] = True
        if nums[0] < subSum + 1:
            dp_arr[0][nums[0]] = True
        for i in range(1, n):
            for j in range(subSum + 1):
                if nums[i] + j < subSum + 1:
                    dp_arr[i][nums[i] + j] = dp_arr[i - 1][j]
                    if dp_arr[i][nums[i] + j] == True and nums[i] + j == subSum:
                        return True
                dp_arr[i][j] = dp_arr[i][j] or dp_arr[i - 1][j]
                # if dp_arr[i][j] == True and j == subSum:  # FIXME , redundant
                #     return True
        return False


if __name__ == '__main__':
    s = Solution()
    cases = [([35, 69, 8, 10, 56, 85, 20, 67, 39, 15, 57, 19, 80, 45, 12, 81, 92, 98, 25, 26, 51, 3, 31, 16, 30, 37, 55,
               52, 61, 17, 30, 82, 52, 85,
               84, 83, 98, 29, 79, 29, 99, 70, 97, 20, 42, 22, 44, 44, 65, 75, 70, 86, 97, 100, 45, 69, 91, 53, 88, 96,
               65, 88, 92, 73, 16, 57, 34, 11
                  , 64, 3, 92, 48, 98, 29, 39, 16, 47, 92, 22, 19, 50, 86, 78, 68, 52, 51, 70, 80, 2, 58, 79, 70, 91,
               94, 23, 47, 81, 4, 18, 15], True),  # gives time exceeded in leetcode
             ([100], False), ([14, 9, 8, 4, 3, 2], True), ([1, 2, 3, 4], True), ([1, 5, 11, 5], True),
             ([1, 2, 3, 5], False),
             ([], False), ([1, 3, 1, 1, 1, 1], True), [(1, 5, 9, 5), True]]

    for input_, expected_return in cases:
        r = s.canPartition(input_)
        assert r == expected_return, f"failure at {input_},expected {expected_return} but returned {r}"
