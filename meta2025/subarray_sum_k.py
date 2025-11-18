"""
https://leetcode.com/problems/subarray-sum-equals-k/description/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days
"""
from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        