"""
https://olp-onesearch.jenkins.release.in.here.com/job/Tools/job/recommendations-training/47/parameters/
"""
from typing import List


# soln idea https://www.geeksforgeeks.org/container-with-most-water/
class Solution:
    def maxArea(self, height: List[int]) -> int:
        if len(height) == 0 or len(height) == 1:
            return 0
        i = 0
        j = len(height) - 1
        maxArea = j * min(height[i], height[j]), i, j
        while i < j:
            min_height = min(height[i], height[j])
            area = (j - i) * min_height
            if area > maxArea[0]:
                maxArea = area, i, j
            if height[i] < height[j]:
                i = i + 1
            else:
                j = j - 1
        return maxArea[0]


if __name__ == '__main__':
    height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    s = Solution()
    r = s.maxArea(height)
    print(r)

