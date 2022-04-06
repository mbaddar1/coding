"""
https://leetcode.com/problems/minimum-window-substring/
"""


class Solution:
    @staticmethod
    def add(str_dict, e):
        if e in str_dict.keys():
            str_dict[e] = str_dict[e] + 1
        else:
            str_dict[e] = 1
        return str_dict

    @staticmethod
    def remove(str_dict, e):
        str_dict[e] = str_dict[e] - 1
        if str_dict[e] == 0:
            del str_dict[e]
        return str_dict

    @staticmethod
    def include(s_dict, t_dict):
        for kt in t_dict:
            if kt in s_dict.keys() and t_dict[kt] == s_dict[kt]:
                pass
            else:
                return False
        return True

    @staticmethod
    def build_dict(t):
        tdict = {}
        for e in t:
            if e in tdict.keys():
                tdict[e] = tdict[e] + 1
            else:
                tdict[e] = 1
        return tdict

    def minWindow(self, s: str, t: str) -> str:
        left = right = 0
        m = len(s)
        n = len(t)
        s_dict = {}
        mode = "expand"
        while right <= m - 1:
            if mode == "expand":
                right += 1

        return


if __name__ == '__main__':
    s = Solution()
    io = [("ADOBECODEBANC", "ABC", "BANC")]
    for e in io:
        assert s.minWindow(e[0], e[1]) == e[2]
