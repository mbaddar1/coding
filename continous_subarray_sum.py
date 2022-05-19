# https://leetcode.com/problems/continuous-subarray-sum/
from typing import List
import numpy as np

# TODO optimize memory usage
"""
Out of memory Error
numpy.core._exceptions._ArrayMemoryError: Unable to allocate 24.5 GiB for an array with shape (57286, 57286) and data type float64
    dp = np.zeros(shape=(n, n))
Line 5 in checkSubarraySum (Solution.py)
    ret = Solution().checkSubarraySum(param_1, param_2)
Line 40 in _driver (Solution.py)
    _driver()
Line 51 in <module> (Solution.py)
test case : https://leetcode.com/submissions/detail/701961972/testcase/ 
"""


class Solution:
    def checkSubarraySum_attempt1(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        # TODO : make memory complexity o(1) or o(n)
        dp = np.zeros(shape=(n, n))
        for i in range(n):
            dp[i][i] = nums[i]
        for i in range(n):
            for j in range(i + 1, n):
                dp[i][j] = dp[i][j - 1] + nums[j]
                if dp[i][j] % k == 0:
                    print(f"Found subarray : {nums[i:j]}")
                    return True
        return False

    def checkSubarraySum(self, nums: List[int], k: int):
        """
        https://leetcode.com/submissions/detail/702604577/testcase/
        # TODO Time limit exceeded https://leetcode.com/problems/continuous-subarray-sum/submissions/
        :param nums:
        :param k:
        :return:
        """
        n = len(nums)
        arr_0_k = np.zeros(n)
        arr_0_k[0] = nums[0]
        for i in range(1, n):
            arr_0_k[i] = arr_0_k[i - 1] + nums[i]
        arr_k_n_1 = np.zeros(n)
        arr_k_n_1[n - 1] = nums[n - 1]
        for j in range(n - 2, -1, -1):
            arr_k_n_1[j] = arr_k_n_1[j + 1] + nums[j]
        tot_sum = arr_0_k[n - 1]  # avoid recalculation of sums
        for i in range(n):
            for j in range(i + 1, n):
                val_low = 0 if i == 0 else arr_0_k[i - 1]
                val_high = 0 if j == n - 1 else arr_k_n_1[j + 1]
                subSum = tot_sum - val_high - val_low
                if subSum % k == 0:
                    print(nums[i:j])
                    return True
        return False


if __name__ == '__main__':
    nums = [23, 2, 4, 6, 7]
    k = 6
    s = Solution()
    r = s.checkSubarraySum(nums, k)
    assert r == True

    ####
    nums = [23, 2, 6, 4, 7]
    k = 6
    s = Solution()
    r = s.checkSubarraySum(nums, k)
    assert r == True

    ###
    nums = [23, 2, 6, 4, 7]
    k = 13
    s = Solution()
    r = s.checkSubarraySum(nums, k)
    assert r == False
