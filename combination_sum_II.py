# https://leetcode.com/problems/combination-sum-ii/
from typing import List


# TODO : find a better way than memoization to avoid re-computing sub-trees
# https://en.wikipedia.org/wiki/Memoization
# https://www.freecodecamp.org/news/memoization-in-javascript-and-react/#:~:text=In%20programming%2C%20memoization%20is%20an,instead%20of%20computing%20it%20again.

class Solution:
    def __init__(self):
        self.memo = set()

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates = sorted(candidates)
        r = self.__combinationSum2(candidates, target)
        r2 = []
        r2_set = set()
        for e in r:
            k = self.create_memo_key(e)
            if k not in r2_set:
                r2_set.add(k)
                r2.append(e)
        return r2

    def create_memo_key(self, candidates):
        key = f"""{','.join(list(map(str, candidates)))}"""
        return key

    def __combinationSum2(self, candidates, target):
        # key = self.create_memo_key(candidates, target)
        # if key == "8:2,5,6,7,10":
        #     print('---')
        # if key in self.memo:
        #     return []
        # self.memo.add(key)
        if len(candidates) == 0:
            return []
        cand_list = []
        if target == candidates[0]:
            return [[candidates[0]]]
        elif target > candidates[0]:
            new_target = target - candidates[0]
            r1 = self.__combinationSum2(candidates[1:], new_target)
            for e in r1:
                tmp = [candidates[0]]
                tmp.extend(e)
                cand_list.append(tmp)
            r2 = self.__combinationSum2(candidates[1:], target)
            for e in r2:
                cand_list.append(e)
        else:
            return []
        return cand_list


if __name__ == '__main__':
    s = Solution()
    r = s.combinationSum2([10, 1, 2, 7, 6, 1, 5], 8)
    print(r)
    r = s.combinationSum2([2, 5, 2, 1, 2], 5)
    print(r)
