from typing import List

import pandas as pd


class Solution:
    STRIDE = 37
    def __init__(self, w: List[int]):

        tot_sum = sum(w)
        self.u = [-1]*tot_sum
        j = 0
        for i in range(len(w)):
            for _ in range(w[i]):
                self.u[j] = i
                j = j+1
        self.curr_idx = Solution.STRIDE % len(self.u)

    def pickIndex(self) -> int:
        val = self.u[self.curr_idx]
        self.curr_idx = (17*self.curr_idx + Solution.STRIDE)%len(self.u)
        return val
if __name__ == '__main__':
    w = [1,3]
    sol = Solution(w)
    r_list = []
    for i in range(100):
        r = sol.pickIndex()
        r_list.append(r)
    counts = pd.Series(r_list).value_counts()
    print(counts)
    pass