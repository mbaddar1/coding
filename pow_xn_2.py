# https://leetcode.com/problems/powx-n/
import numpy as np


class Solution:
    def bitwise_log2(self, n):
        u = n
        counter = 0
        while u:
            u = u >> 1
            counter += 1
        return counter - 1

    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1.0
        sign = 1 if n > 0 else -1
        n = abs(n)
        u = self.bitwise_log2(n)
        r = n - (1 << u)
        acc = x
        for i in range(u):
            acc *= acc
        for j in range(r):
            acc *= x
        ret = acc if sign >= 0 else 1 / acc
        return ret


if __name__ == '__main__':
    s = Solution()
    # r = s.bitwise_log2(16)
    # print(r)
    r = s.myPow(2., -2)
    print(r)
