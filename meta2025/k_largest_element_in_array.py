# https://leetcode.com/problems/kth-largest-element-in-an-array/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days
import heapq
from typing import List

import numpy as np
from tqdm import tqdm


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        n = len(nums)
        assert k <= n
        heap_ = nums[:k]
        heapq.heapify(heap_)
        for v in nums[k :]:
            if v > heap_[0]:
                h = heapq.heappop(heap_)
                heapq.heappush(heap_,v)
        return heap_[0]


if __name__ == "__main__":
    sol = Solution()
    a = [3,2,1,5,6,4]
    k = 2
    r = sol.findKthLargest(a, k)
    assert r == 5

    nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
    k = 4
    r = sol.findKthLargest(nums, k)
    assert r == 4


    #### Big Test #####
    #
    num_min = -10e4
    num_max = 10e4
    max_size = 10000
    num_tests = 1000
    sol = Solution()
    for _ in tqdm(range(num_tests), desc="test"):
        size = np.random.randint(low=2, high=max_size)
        k = np.random.randint(low=1, high=size)
        arr = []
        for _ in range(size):
            v = np.random.randint(low=num_min, high=num_max)
            arr.append(v)
        sorted_arr = sorted(arr)  # O(nlogn)
        expected_results = sorted_arr[-k]
        r = sol.findKthLargest(arr, k)
        assert r == expected_results
