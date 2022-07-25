# https://leetcode.com/problems/merge-intervals/
from typing import List
from functools import cmp_to_key


def compare(a, b):
    return a[0] - b[0]


class Solution:
    @staticmethod
    def compare(a, b):
        return a[0] - b[0]

    def merge_two(self, interval1, interval2):
        if interval1[1] >= interval2[0]:
            return [min(interval1[0], interval2[0]), max(interval1[1], interval2[1])]
        else:
            return []

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key=cmp_to_key(compare))
        i = 0
        n = len(intervals)

        while i < n - 1:
            m = self.merge_two(intervals[i], intervals[i + 1])
            if not m:
                i = i + 1
            else:
                intervals[i] = m
                del intervals[i + 1]
                n = len(intervals)

        return intervals


if __name__ == '__main__':
    intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
    s = Solution()
    r = s.merge(intervals)
    print(r)

    intervals = [[1, 4], [4, 5]]
    r = s.merge(intervals)
    print(r)

    intervals = [[1, 10], [2, 9]]
    r = s.merge(intervals)
    print(r)