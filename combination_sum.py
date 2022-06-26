"""
https://leetcode.com/problems/combination-sum/
https://www.interviewbit.com/blog/combination-sum/
"""
from typing import List, Union, Tuple


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        rx = self.__combinationSum(candidates, target)
        return rx

    def __combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        if len(candidates) == 1:
            num = candidates[0]
            if target % num == 0:
                cnt = int(target / num)
                r = [num for _ in range(cnt)]
                return [r]
            else:
                return []
        r3 = []
        if target % candidates[0] == 0:
            cnt = int(target / candidates[0])
            r0 = [candidates[0] for _ in range(cnt)]
            r3.append(r0)

        counter = 0
        while (counter * candidates[0]) < target:
            residual = target - counter * candidates[0]
            # tmp = [(counter, candidates[0])]

            r2 = self.__combinationSum(candidates[1:], residual)
            if len(r2) != 0:
                for k in range(len(r2)):
                    # if counter > 0:
                    tmp = [candidates[0] for _ in range(counter)]
                    tmp.extend(r2[k])
                    r3.append(tmp)

            counter = counter + 1
        return r3


if __name__ == '__main__':
    s = Solution()
    # r = s.combinationSum([2, 3, 6, 7], 7)
    # print(r)
    r = s.combinationSum([1, 3, 4, 5, 6], 4)
    print(r)
