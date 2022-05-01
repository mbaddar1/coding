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
        if tot_Sum % 2 != 0:
            return False
        subSum = int(tot_Sum / 2)
        dp_arr = np.full(shape=(n, subSum + 1), fill_value=False)
        dp_arr[0][0] = True
        dp_arr[0][nums[0]] = True
        for i in range(1, n):
            max_ = subSum - nums[i]
            for j in range(max_ + 1):
                dp_arr[i][nums[i] + j] = dp_arr[i - 1][j]
                if dp_arr[i][nums[i] + j] == True and nums[i] + j == subSum:
                    return True
                dp_arr[i][j] = dp_arr[i][j] or dp_arr[i - 1][j]
                # if dp_arr[i][j] == True and j == subSum:  # FIXME , redundant
                #     return True
        return False


if __name__ == '__main__':
    s = Solution()

    cases = [([1, 2, 3, 4], True), ([1, 5, 11, 5], True), ([1, 2, 3, 5], False)]
    for input_, expected_return in cases:
        r = s.canPartition(input_)
        assert r == expected_return, f"failure at {input_},expected {expected_return} but returned {r}"
