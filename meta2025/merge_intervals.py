# https://leetcode.com/problems/merge-intervals/description/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days
# accepted
#https://leetcode.com/problems/merge-intervals/submissions/1826940393
import random
from typing import List, Tuple, Optional, Iterable



class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals_sorted = sorted(intervals, key=lambda x: x[0])
        merged_list = []
        curr_interval = intervals_sorted[0]
        n = len(intervals_sorted)
        for i in range(1,n):
            if curr_interval[1]>=intervals_sorted[i][0]: #mergeable
                curr_interval_lb = int(min(curr_interval[0], intervals_sorted[i][0]))
                curr_interval_ub = int(max(curr_interval[1], intervals_sorted[i][1]))
                curr_interval = [curr_interval_lb,curr_interval_ub]

            else:
                merged_list.append(curr_interval)
                curr_interval = intervals_sorted[i]
        merged_list.append(curr_interval)
        return merged_list




if __name__ == '__main__':
    a = [[15,18],[2,6],[1,3],[8,10]]
    s = Solution()
    r = s.merge(a)
    print(r)

    ###
    a =  [[4,7],[1,4]]
    r = s.merge(a)
    print(r)



