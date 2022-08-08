# https://leetcode.com/problems/wildcard-matching/
"""
Incorrect test case
https://leetcode.com/submissions/detail/767065530/
Input:
"aa"
"*"
Output:
false
Expected:
true

"""


class Solution:
    # based on default regex understanding ( * must be preceded by character, not a lone)
    @staticmethod
    def findall(chr, s):
        pos = []
        for i, c in enumerate(s):
            if c == chr:
                pos.append(i)
        return pos

    def isMatch(self, s: str, p: str):

        return Solution.__isMatch(s, p)

    @staticmethod
    def __isMatch(s: str, p: str):

        if not (s or p):
            return True
        elif s and not p:
            return False
        elif not s and (p and "".join(set(p)) != '*'):
            return False

        n_p = len(p)
        n_s = len(s)
        if p[0] == '?':
            return Solution.__isMatch(s[1:], p[1:])
        elif p[0] == '*':
            if n_p == 1:
                return True
            else:

                next_chr = p[1]
                if next_chr == '*':
                    return Solution.__isMatch(s, p[1:])
                elif next_chr == '?':
                    for i in range(n_s):
                        if Solution.__isMatch(s=s[i:], p=p[1:]):
                            return True
                    return False
                else:
                    positions = Solution.findall(chr=next_chr, s=s)
                    for pos in positions:
                        # print(f'trying p = {p[1:]} vs s= {s[pos:]}')
                        if Solution.__isMatch(s[pos:], p[1:]):
                            # print('Success')
                            return True
                        # else:
                        #     # print('Failure')

                    return False
        else:
            if p[0] == s[0]:
                return Solution.__isMatch(s[1:], p[1:])
            return False

    def isMatch_2(self, s: str, p: str):
        n_p = len(p)
        n_s = len(s)
        i_p = 0
        i_s = 0
        q = {}
        while i_p < n_p:
            s_remaining = s[i_s:]
            p_remaining = p[i_p:]
            if p[i_p] == '?':
                i_p += 1
                i_s += 1
            elif p[i_p] == '*':
                if i_p == n_p - 1:
                    return True
                else:
                    next_chr = p[i_p + 1]
                    while i_s < n_s and s[i_s] != next_chr:
                        i_s += 1
                    i_p += 1
            else:
                if i_s < n_s and s[i_s] == p[i_p]:
                    i_s += 1
                    i_p += 1
                elif not q:
                    return False
                else:
                    i_s, i_p = q.pop()
        if i_p == n_p and i_s == n_s:
            return True
        return False

    def isMatch_1(self, s: str, p: str) -> bool:
        n_s = len(s)
        n_p = len(p)
        i_s = 0
        i_p = 0
        if p == '*':
            return True
        while i_p < n_p:
            if i_p < n_p - 1 and p[i_p + 1] == '*':
                is_star_last = i_p + 1 == n_p - 1
                if p[i_p] == '?':
                    if is_star_last:
                        return True
                    else:
                        next_chr = p[i_p + 2]  # assume minimal pattern (normalized , no ?*?*)
                        while i_s < n_s and s[i_s] != next_chr:
                            i_s += 1
                else:
                    while i_s < n_s and s[i_s] == p[i_p]:
                        i_s += 1
                i_p += 2


            else:
                if p[i_p] == '?':
                    i_s += 1
                    i_p += 1
                elif i_s < n_s and p[i_p] == s[i_s]:
                    i_p += 1
                    i_s += 1
                else:
                    return False
        if i_p == n_p and i_s == n_s:
            return True
        return False


if __name__ == '__main__':
    s = Solution()
    # assert s.isMatch(s="a", p="*") == True
    # assert s.isMatch(s="aa", p="aa") == True
    # assert s.isMatch(s="a", p="ba") == False
    # assert s.isMatch(s='ba', p='?a') == True
    # assert s.isMatch(s='abc', p='a?*')
    # assert s.isMatch(s='axybc', p='a*bc') == True
    # assert s.isMatch(s="axyzbc", p='*a*bc')
    # assert s.isMatch(s='axycb', p='a?*bc') == False
    # assert s.isMatch(s="bcxy", p="*xy") == True
    # assert s.isMatch(s="", p="*") == True
    # assert s.isMatch(s="b", p="*b") == True
    # assert s.isMatch(s="bc", p="b*c") == True
    # # # failed to correct test cases
    # assert s.isMatch(s="aa", p="*") == True
    # https://leetcode.com/submissions/detail/767935531/
    # assert s.isMatch(s="adceb", p="*a*b") == True
    # https://leetcode.com/submissions/detail/767943077/
    # assert s.isMatch(s="abcabczzzde", p="*abc???de*") == True
    # https://leetcode.com/submissions/detail/768653890/
    # assert s.isMatch(s="", p="***********")
    # assert s.isMatch(s="hi", p="*?")
    # TODO last failure  https://leetcode.com/submissions/detail/768675557/
    assert s.isMatch(
        s="babbbbaabababaabbababaababaabbaabababbaaababbababaaaaaabbabaaaabababbabbababbbaaaababbbabbbbbbbbbbaabbb",
        p="b**bb**a**bba*b**a*bbb**aba***babbb*aa****aabb*bbb***a")
