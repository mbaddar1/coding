"""
https://leetcode.com/problems/find-all-anagrams-in-a-string/
"""


# def is_anagram(s, dictt):
#     dictt_copy = dictt.copy()
#     n = len(s)
#     for i in range(n):
#         if s[i] in dictt_copy.keys():
#             v = dictt_copy[s[i]]
#             dictt_copy[s[i]] = v - 1
#         else:
#             return False
#     for v in dictt_copy.values():
#         if v != 0:
#             return False
#
#     return True


def build_dict(p):
    dictt = dict()
    m = len(p)
    for i in range(m):
        if p[i] in dictt.keys():
            v = dictt[p[i]]
            dictt[p[i]] = v + 1
        else:
            dictt[p[i]] = 1
    return dictt


def update_dict(dictt, add, remove):
    # add a
    if add in dictt.keys():
        v = dictt[add]
        dictt[add] = v + 1
    else:
        dictt[add] = 1
    # remove b
    if remove in dictt.keys():
        v = dictt[remove]
        dictt[remove] = v - 1
        if dictt[remove] == 0:
            del dictt[remove]
        else:
            pass
    return dictt


def compare_dict(dict1, dict2):
    if len(dict1) != len(dict2):
        return False
    for k in dict1.keys():
        if k in dict2.keys():
            if dict1[k] != dict2[k]:
                return False
        else:
            return False
    return True


class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """

        n = len(s)
        m = len(p)
        if s == 0:
            return []
        if p == 0:
            return []
        if n < m:
            return []

        i = 0
        res = []
        pdictt = build_dict(p)
        sdictt = None
        while (i + m - 1) < n:
            if sdictt is None:
                sdictt = build_dict(s[i:i + m])
            else:
                sdictt = update_dict(sdictt, s[i + m-1], s[i - 1])
            if compare_dict(sdictt, pdictt):
                res.append(i)
            i = i + 1
        return res


if __name__ == '__main__':
    sol = Solution()
    s = "cbaebabacd"
    p = "abc"
    res = sol.findAnagrams(s, p)
    assert set(res) == {0, 6}

    s = "abab"
    p = "ab"
    res = sol.findAnagrams(s, p)
    assert set(res) == {0, 1, 2}
