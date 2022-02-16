"""
https://leetcode.com/explore/interview/card/facebook/53/recursion-3/307/
"""


def getNextChar(i, s):
    n = len(s)
    if i + 1 > n - 1:
        return None
    return s[i + 1]


class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if len(s) == 0 and len(p) == 0:
            return True
        elif len(s) > 0 and len(p) == 0:
            return False
        elif len(s) == 0 and len(p) > 0:
            return False
        if p[0] == '.':
            c = getNextChar(0, p)
            if c is not None and c == '*':
                m = len(s)
                flag = False
                j = 0
                while j < m and flag is not True:
                    flag = self.isMatch(s[(j + 1):], p[2:])
                    j += 1
                return flag
            elif c is not None and c != '*':
                return self.isMatch(s[1:], p[1:])
            else:
                return self.isMatch(s[1:], p[1:])
        else:
            c = getNextChar(0, p)
            if c is not None and c == '*':
                m = len(s)
                flag = False
                j = 0
                while j < m and flag is not True:
                    flag = s[j] == p[0] and self.isMatch(s[(j + 1):], p[2:])
                    j += 1
                return flag
            elif c is not None and c != '*':
                return p[0] == s[0] and self.isMatch(s[1:], p[1:])
            else:
                return p[0] == s[0] and self.isMatch(s[1:], p[1:])


if __name__ == '__main__':
    sol = Solution()
    # s = "aa"
    # p = "a"
    # sol = Solution()
    # r = sol.isMatch(s, p)
    # print(r)

    s = "aa"
    p = "a*"
    r = sol.isMatch(s, p)
    print(r)
