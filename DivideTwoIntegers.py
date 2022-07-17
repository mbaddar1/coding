# https://leetcode.com/problems/divide-two-integers/

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == 0:
            return 0
        if dividend > 0 and divisor > 0 or dividend < 0 and divisor < 0:
            sign = 1
        else:
            sign = -1
        super_divisor = divisor
        exp_counter = 0
        while dividend > super_divisor:
            super_divisor += super_divisor
            exp_counter += 1
        remainder = super_divisor - dividend
        counter = 0
        while remainder > 0:
            remainder -= divisor
            counter += 1

        res = (1 << exp_counter) - counter
        res = res if sign > 0 else -res
        return res


if __name__ == '__main__':
    s = Solution()
    assert s.divide(100, 3) == 33
    assert s.divide(99, 3) == 33
    assert s.divide(98,3) == 32
    assert s.divide(1, 3) == 0
    assert s.divide(0, 3) == 0
    assert s.divide(5, 3) == 1

