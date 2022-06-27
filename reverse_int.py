"""
https://leetcode.com/problems/reverse-integer/
"""


class Solution:

    def reverse(self, x: int) -> int:
        nbits = 9
        MAX_INT = 1 << (nbits - 1) - 1
        MIN_INT_U = 1 << (nbits - 1)

        if abs(x) < 10:
            return x
        if x > MAX_INT or x < -MIN_INT_U:
            return 0
        sign = 1 if x > 0 else -1

        y = abs(x)
        num = 0
        while y != 0:
            mod_ = y % 10
            the_max = MAX_INT if sign > 0 else MIN_INT_U

            if the_max - mod_ < num * 10:
                return 0
            if the_max - num * 10 < mod_:
                return 0
            num = mod_ + num * 10
            y = int(y / 10)
        return sign * num


if __name__ == '__main__':
    s = Solution()
    r = s.reverse(-255)
    print(r)
