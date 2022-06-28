"""
https://leetcode.com/problems/permutations/
"""
from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        indices_init = [i for i in range(len(nums))]
        r = self.permute_aux(nums, indices_init)
        return r

    def permute_aux(self, nums, indices):
        if len(indices) == 1:
            return [[nums[indices[0]]]]
        set_ = set(indices)
        r2 = []
        for i in indices:
            indices_diff_i = set_.difference(set([i]))
            r = self.permute_aux(nums, list(indices_diff_i))

            for e in r:
                tmp = [nums[i]]
                tmp.extend(e)
                r2.append(tmp)
        return r2


if __name__ == '__main__':
    s = Solution()
    r = s.permute([1, 2, 3])
    print(r)
