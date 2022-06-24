"""
https://leetcode.com/problems/3sum/
"""
from typing import List

import numpy as np


class Solution:
    def twoSum(self, nums):
        sum_dict = {}
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] + nums[j] in sum_dict.keys():
                    sum_dict[nums[i] + nums[j]].append((i, j))
                else:
                    sum_dict[nums[i] + nums[j]] = [(i, j)]
        return sum_dict

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        if n < 3:
            return []
        dict_ = self.twoSum(nums)
        res = []

        for i in range(n):
            if -nums[i] in dict_.keys():
                v = dict_[-nums[i]]
                for k in v:
                    if k[0] != i and k[1] != i:
                        q = []
                        q.append(nums[k[0]])
                        q.append(nums[k[1]])
                        q.append(nums[i])
                        q = np.sort(q)
                        q = (q[0], q[1], q[2])
                        if not q in res:
                            res.append(q)
                del dict_[-nums[i]]
        return res


if __name__ == '__main__':
    nums = [-1, 0, 1, 2, -1, -4]
    s = Solution()
    r = s.threeSum(nums)
    print(r)
