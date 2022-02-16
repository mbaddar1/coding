"""
https://leetcode.com/problems/partition-equal-subset-sum/solution/
"""
import numpy as np


def containsSum(sum, nums, i, memo):
    if sum == 0:
        return True
    if sum < 0:
        return False
    # sum >0
    n = len(nums)
    if n == 0:
        return False
    if i == n:
        return False
    if i < n - 1 and memo[i + 1][sum - nums[i]] != -1:
        path1 = memo[i + 1][sum - nums[i]]
        print('memo')
    else:
        path1 = containsSum(sum - nums[i], nums, i + 1, memo)
        if i < n - 1:
            memo[i + 1][sum - nums[i]] = path1
    if i < n - 1 and memo[i + 1][sum] != -1:
        print('memo')
        path2 = memo[i + 1][sum]
    else:
        path2 = containsSum(sum, nums, i + 1, memo)
        if i < n - 1:
            memo[i + 1][sum] = path2

    return bool(path1) or bool(path2)


class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        sum_ = 0
        for i in range(len(nums)):
            sum_ += nums[i]
        if sum_ % 2 > 0:
            return False
        subSum = int(sum_ / 2)
        memo = np.empty(shape=(len(nums), subSum+1), dtype=int)
        memo.fill(-1)
        r = containsSum(subSum, nums, 0, memo)

        return r


if __name__ == '__main__':
    sol = Solution()
    nums = [1, 2, 3, 4]
    r = sol.canPartition(nums)
    assert r == True

    sol = Solution()
    nums = [1, 2, 3, 5]
    r = sol.canPartition(nums)
    assert r == False

    sol = Solution()
    nums = [1, 5, 11, 5]
    r = sol.canPartition(nums)
    assert r == True

    nums = [14,75,64,20,95,78,6,98,77,4,71,66,78,44,4,46,77,46,4,84,18,14,52,5,89,26,12,48,71,35,57,10,59,69,35,70,34,
            80,80,66,91,9,36,91,85,24,46,45,54,86,3,40,30,23,24,4,88,50,42,25,41,60,27,47,92,92,49,50,56,94,9,82,49,41,
            18,1,23,85,8,48,55,59,82,82,12,84,47,45,41,28,22,15,50,9,64,91,6,94,14,31]
    r = sol.canPartition(nums)
    assert r == True
