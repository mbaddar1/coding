# https://leetcode.com/problems/first-missing-positive/
"""
Assumptions:
1) Numbers are distinct
"""
from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # https://www.geeksforgeeks.org/find-the-smallest-positive-number-missing-from-an-unsorted-array/
        N = len(nums)
        one_exists = False
        for i, num in enumerate(nums):
            if num == 1:
                one_exists = True
        if not one_exists:
            return 1
        for i, num in enumerate(nums): # make range of nums[i] : 1<=nums[i]<=N
            if num <= 0 or num > N:
                nums[i] = 1
        for i, num in enumerate(nums): # mark each nums[i]. When an integer is missing, it will miss the mark.
            idx = (nums[i] - 1) % N
            nums[idx] += N
        for i, num in enumerate(nums): # find the needed number
            if num < N + 1:
                return i + 1
        return N + 1


if __name__ == '__main__':
    nums = [2, 1]
    nums = [3, 4, -1, 1]
    nums = [7, 8, 9, 11, 12]
    s = Solution()
    r = s.firstMissingPositive(nums)
    print(r)
