"""
https://leetcode.com/problems/zigzag-conversion/description/
success
https://leetcode.com/problems/zigzag-conversion/submissions/1850993455
"""


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1: # Take care : missing this case led to time limit exceeded
            return s
        n = len(s)
        big_step = 2 * (numRows - 1)
        secondary_step = 2 * (numRows - 2)
        res = ""
        for i in range(numRows):
            j = i
            while j < n:
                res += s[j]
                if 0 < i < numRows - 1:
                    j1 = j + secondary_step
                    if j1 < n:
                        res += s[j1]
                j += big_step

            if i > 0:
                secondary_step -= 2

        return res


if __name__ == "__main__":

    sol = Solution()
    s = "A"
    res = sol.convert(s, 1)
    assert res == "A"

    s = "ABCD"
    res = sol.convert(s, 2)
    assert res == "ACBD"

    s = "PAYPALISHIRING"
    res = sol.convert(s, 3)
    assert res == "PAHNAPLSIIGYIR"

    s = "PAYPALISHIRING"
    res = sol.convert(s, 4)
    assert res == "PINALSIGYAHRPI"
