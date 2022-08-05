# https://leetcode.com/problems/trapping-rain-water/
# https://leetcode.com/problems/trapping-rain-water/submissions/
from typing import List

import numpy as np


class Solution:

    def trap(self, height: List[int]) -> int:
        N = len(height)
        cum = np.zeros(N)
        cum[0] = height[0]
        for i in range(1, N):
            cum[i] = cum[i - 1] + height[i]

        # fw
        i = 0
        while i < N and height[i] == 0:
            i += 1
        max_idx = i
        i += 1
        counter = 0
        while i < N:
            if height[i] > height[max_idx]:
                the_height = min(height[i], height[max_idx])
                width = i - max_idx - 1
                fillers = cum[i] - cum[max_idx] - height[i]

                area = the_height * width - fillers
                counter += area
                max_idx = i
            i += 1
        # bw
        i = N - 1
        while i >= 0 and height[i] == 0:
            i -= 1
        max_idx = i
        i -= 1
        while i >= 0:
            if height[i] >= height[max_idx]:
                the_height = min(height[i], height[max_idx])
                width = max_idx - i - 1
                fillers = cum[max_idx] - cum[i] - height[max_idx]
                area = the_height * width - fillers
                counter += area
                max_idx = i
            i -= 1

        return counter


if __name__ == '__main__':
    s = Solution()

    height = [0]
    assert s.trap(height) == 0

    height = [0, 7, 1, 4, 6]
    assert s.trap(height) == 7

    height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    assert s.trap(height) == 6

    height = [4, 2, 0, 3, 2, 5]
    assert s.trap(height) == 9

    height = [4, 2, 3]
    assert s.trap(height) == 1

    height = [2, 4, 2]
    assert s.trap(height) == 0

    height = [2, 0, 2]
    assert s.trap(height) == 2

    height = [4, 1, 3, 6]
    assert s.trap(height) == 4
