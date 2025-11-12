"""
https://leetcode.com/problems/longest-substring-without-repeating-characters/description/?envType=featured-list&envId=top-interview-questions?envType=featured-list&envId=top-interview-questions

Status
Solution Submitted and
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        if n <= 1:
            return n
        max_len = 1
        existence_dict = {s[0]: 0}
        start = 0
        for i in range(1, len(s)):
            c = s[i]
            if i == n - 1:
                if c in existence_dict.keys():
                    max_len = max(max_len, i - start)
                    # print(f"{s[start:i]}->{max_len}")
                else:
                    max_len = max(max_len, i - start + 1)
                    # print(f"{s[start:(i+1)]}->{max_len}")
            elif c in existence_dict.keys():
                max_len = max(max_len, i - start)
                # print(f"{s[start:i]}->{max_len}")
                j = existence_dict[s[i]]
                if j < (n - 1):
                    start = j + 1
                tmp = []
                for k, v in existence_dict.items():
                    if v < start:
                        tmp.append(k)
                for u in tmp:
                    del existence_dict[u]

            existence_dict[c] = i
        return max_len


if __name__ == '__main__':
    # 1
    s = "abcdab"
    # 2
    # s = "ababcdef"
    # 3
    # s = "pwwkew"
    # 4
    # s = "tmmzxft"
    # 5
    # s = "k"
    sol = Solution()
    r = sol.lengthOfLongestSubstring(s)
    print(r)
