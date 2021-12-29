"""
https://leetcode.com/explore/interview/card/facebook/5/array-and-strings/3008/
Given a string s, find the length of the longest substring without repeating characters.



Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.


Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.
"""


class Solution(object):
    def lengthOfLongestSubstring_attempt1_wrong(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        ch_dict = dict()
        counter = 0
        max_ = 0
        for i in range(n):
            if s[i] in ch_dict.keys():
                max_ = max(max_, counter)
                last_i = ch_dict[s[i]]
                counter = i - last_i
                ch_dict.clear()
                ch_dict[s[i]] = i
            else:  # block (1)
                ch_dict[s[i]] = i
                counter = counter + 1
        max_ = max(max_, counter)
        return max_
        # TODO focus in edge case, this line of the string stretched to end, esp for block(1)

    def lengthOfLongestSubstring(self, s):
        n = len(s)
        if n <= 1:
            return n

        i = 0
        j = 1
        max_ = 0
        chr_dict = {s[i]: i}
        while j < n:
            if s[j] in chr_dict.keys() and chr_dict[s[j]] >= i:
                count_ = j - chr_dict[s[j]]
                max_ = max(max_, count_)
                i = chr_dict[s[j]] + 1
            else:
                count_ = j - i + 1
                max_ = max(max_, count_)
            chr_dict[s[j]] = j
            j = j + 1

        return max_


if __name__ == '__main__':
    s = "abcabcbb"
    sol = Solution()
    l = sol.lengthOfLongestSubstring(s)
    assert l == 3

    s = "bbbbb"
    sol = Solution()
    l = sol.lengthOfLongestSubstring(s)
    assert l == 1

    s = "pwwkew"
    sol = Solution()
    l = sol.lengthOfLongestSubstring(s)
    assert l == 3

    s = "abcdefg"
    sol = Solution()
    l = sol.lengthOfLongestSubstring(s)
    assert l == 7

    assert sol.lengthOfLongestSubstring("aab") == 2

    assert sol.lengthOfLongestSubstring("dvdf") == 3

    assert sol.lengthOfLongestSubstring("abba") == 2

    assert sol.lengthOfLongestSubstring("bbabcddcea") == 4
