# https://leetcode.com/problems/regular-expression-matching/
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        i_p = 0
        i_s = 0
        n_p = len(p)
        n_s = len(s)
        while i_p < n_p and i_s < n_s:
            if p[i_p] == '.':
                if i_p < n_p - 1 and p[i_p + 1] == '*':
                    while i_s < n_s:
                        i_s += 1
                    i_p += 2
                else:
                    i_s += 1
                    i_p += 1
            else:  # not '.'
                if i_p < n_p - 1 and p[i_p + 1] == '*':
                    while i_s < n_s and p[i_p] == s[i_s]:
                        i_s += 1
                    i_p += 2
                else:
                    if p[i_p] == s[i_s]:
                        i_s += 1
                        i_p += 1
                    else:
                        break

        if i_p == n_p and i_s == n_s:
            return True
        return False


if __name__ == '__main__':
    s = "aa"
    p = "a"
    q = Solution()
    print(q.isMatch(s, p))

    s = "aa"
    p = "a*"
    print(q.isMatch(s, p))

    s = "ab"
    p = ".*"
    print(q.isMatch(s, p))
