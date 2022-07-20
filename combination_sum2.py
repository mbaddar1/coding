# https://leetcode.com/problems/combination-sum/
from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates = sorted(candidates)
        r = self.__combinationSum(candidates, target)
        return r

    def __combinationSum(self, candidates, target):
        if len(candidates) == 0:
            return []
        cand_list = []
        if target == candidates[0]:
            return [[candidates[0]]]
        elif target > candidates[0]:
            r1 = self.__combinationSum(candidates, target - candidates[0])
            for e in r1:
                tmp = [candidates[0]]
                tmp.extend(e)
                cand_list.append(tmp)
            r2 = self.__combinationSum(candidates[1:], target)
            for e in r2:
                cand_list.append(e)
        else:
            return []
        return cand_list


if __name__ == '__main__':
    s = Solution()
    r = s.combinationSum([2, 3, 6, 7], 7)
    print(r)
    r = s.combinationSum([2, 3, 5], 8)
    print(r)
    pass
