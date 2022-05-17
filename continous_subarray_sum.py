from typing import List
import numpy as np


class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        n = len(nums)
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
