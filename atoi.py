"""
https://leetcode.com/problems/string-to-integer-atoi/
"""
from typing import Tuple


def remove_whitespace(s):
    for i, c in enumerate(s):
        if c != ' ':
            break
    return i


def get_sign(s: str) -> Tuple:
    if s[0] == '-':
        return -1, 1
    elif s[1] == '+':
        return 1, 1
    else:
        return 1, 0


def get_numeric_part(s: str) -> int:
    for i, c in enumerate(s):
        if not c.isdigit():
            break
    return max(0, i - 1)


def convert_to_int(s, sign):
    MAX_INT = (1 << 31) - 1
    MIN_INT_U = (1 << 31)
    int_ = 0
    for c in s:
        c_val = ord(c) - ord('0')
        if sign == 1:
            if c_val > MAX_INT - int_ * 10:
                return MAX_INT
        if sign == -1:
            if c_val > MIN_INT_U - int_ * 10:
                return MIN_INT_U
        int_ = int_ * 10 + c_val
    return int_


def atoi(s: str) -> int:
    idx = remove_whitespace(s)
    s = s[idx:]

    sign, idx = get_sign(s)
    s = s[idx:]

    idx = get_numeric_part(s)
    s = s[:idx + 1]

    int_ = sign * convert_to_int(s, sign)
    return int_


if __name__ == '__main__':
    #int_ = atoi("     -42 I am happy")
    # s1 = str((1 << 32) - 1)
    # s2 = str(-1 * (1 << 32))
    #print(int_)
    int2_ = atoi("-429496729555")
    print(int2_)
