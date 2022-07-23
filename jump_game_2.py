# https://leetcode.com/problems/jump-game-ii/
from typing import List

import numpy as np


class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        min_jumps = list(np.arange(n))
        change = False
        while not change:
            for i in range(n):
                target = min_jumps[i] + nums[i]
                if target < n and min_jumps[i] + 1 < min_jumps[target]:
                    min_jumps[target] = min_jumps[i] + 1
                    change = True
        return min_jumps[n - 1]


if __name__ == '__main__':
    s = Solution()
    r = s.jump([2, 3, 1, 1, 4])
    print(r)
    r = s.jump([2, 3, 0, 1, 4])
    print(r)
    r = s.jump([4, 3, 0, 1, 4])
    print(r)
    r = s.jump([0, 1, 2, 3, 4])
    print(r)

