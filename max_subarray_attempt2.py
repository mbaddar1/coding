# https://leetcode.com/problems/maximum-subarray/
from typing import List

import numpy as np


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sum_ = sum(nums)

        cumsum1 = np.zeros(len(nums))
        cumsum1[0] = nums[0]
        for i in range(1, len(nums)):
            cumsum1[i] = nums[i] + cumsum1[i - 1]
        cumsum2 = np.zeros(len(nums))
        cumsum2[len(nums) - 1] = nums[len(nums) - 1]

        for j in range(len(nums) - 2, -1, -1):
            cumsum2[j] = cumsum2[j + 1] + nums[j]
        min1 = min(cumsum1)
        min2 = min(cumsum2)
        i = list(cumsum1).index(min1)
        j = list(cumsum2).index(min2)
        if i > j:
            return 0
        if cumsum1[i] < 0:
            sum_ = sum_ - cumsum1[i]
        if cumsum2[j] < 0:
            sum_ = sum_ - cumsum2[j]

        if sum_ > 0:
            return sum_
        else:
            return 0


if __name__ == '__main__':
    # a = [1]
    # a = [5, 4, -1, 7, 8]
    # a = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    a = [-1, -1]
    s = Solution()
    r = s.maxSubArray(a)
    print(r)
