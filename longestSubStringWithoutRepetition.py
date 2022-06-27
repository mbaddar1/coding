class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        if n == 1:
            return 1
        i = 0
        j = 0
        max_len = j - i + 1
        dict_ = dict()
        dict_[s[0]] = ""
        while j < n:
            j = j + 1
            if j < n:
                while s[j] in dict_.keys():
                    del dict_[s[i]]
                    i = i + 1
                dict_[s[j]] = ""
                max_len = max(max_len, j - i + 1)

        return max_len


if __name__ == '__main__':
    q = Solution()
    r = q.lengthOfLongestSubstring("abcabcbb")
    print(r)
    r = q.lengthOfLongestSubstring("bbbbb")
    print(r)

    r = q.lengthOfLongestSubstring("pwwkew")
    print(r)
    r = q.lengthOfLongestSubstring("a")
    print(r)
    r = q.lengthOfLongestSubstring("abcde")
    print(r)