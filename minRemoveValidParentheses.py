"""
https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/
https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/submissions/
"""


class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        new_s = ""
        lpar_counter = 0
        for c in s:
            if c == '(':
                lpar_counter += 1
                new_s += str(c)
            elif c == ')':
                if lpar_counter > 0:
                    lpar_counter -= 1
                    new_s += str(c)
            else:
                new_s += str(c)

        n = len(new_s)
        new_s2 = ""
        rpar_counter = 0
        for i in range(n - 1, -1, -1):
            c = new_s[i]
            if c == ')':
                rpar_counter += 1
                new_s2 = str(c) + new_s2
            elif c == '(':
                if rpar_counter > 0:
                    rpar_counter -= 1
                    new_s2 = str(c) + new_s2

            else:
                new_s2 = str(c) + new_s2
        return new_s2


if __name__ == '__main__':
    s = Solution()
    io = [("lee(t(c)o)de)", "lee(t(c)o)de"), ("a)b(c)d", "ab(c)d"), ("))((", "")]
    for e in io:
        assert s.minRemoveToMakeValid(e[0]) == e[1]
