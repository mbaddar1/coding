"""
https://leetcode.com/problems/combination-sum/description/
DONE
https://leetcode.com/problems/combination-sum/submissions/1863442612/
"""
from typing import List


class Solution:
    def __init__(self):
        self.candidates_set = None
        self.memoization = set() # TODO didnot work, to check later
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.candidates_set = set(candidates)
        r =  self.__comb_sum(candidates,target)
        # FIXME workaround to avoid duplicates
        #   Tried to genuinely to fix it using memoization but failed

        tmp_set = set()
        for u in r:
            tmp_set.add(tuple(u))
        r2 = [list(k) for k in tmp_set]
        return r2

    def __comb_sum(self,candidates: List[int], target: int):
        combs = []
        if target <=1:
            print("target <= 1, returning[]")
            return []
        if target in self.candidates_set:
            print(f"target= {target} in candidates_set")
            combs.append([target])
        print("going over candidates")
        for candidate in candidates:
            new_target = target - candidate

            print(f"new_target=target-candidate, {target}-{candidate} = {new_target}")
            sub_combs = self.__comb_sum(candidates,new_target)
            print(f"sub_combs for new_target = {new_target}", sub_combs)
            #if len(sub_combs) > 0:
            #    self.memoization.add(tuple(sorted([candidate,new_target])))
            for sub_comb in sub_combs:
                combs.append(sorted([candidate]+sub_comb))
            print(f"combs = {combs}")
        return combs
if __name__=="__main__":
    candidates = [2, 3, 6, 7]
    target = 7
    sol = Solution()
    r = sol.combinationSum(candidates,target)
    print(r)
    print("============")
    candidates = [2,3,5]
    target = 8
    r = sol.combinationSum(candidates,target)
    print(r)
