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
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        ch_set = set()
        counter = 0
        max_ = 0
        for i in range(n):
            if s[i] in ch_set:
                ch_set.clear()
                max_ = max(max_, counter)
                counter = 0
            else:  # block (1)
                ch_set.add(s[i])
                counter = counter + 1
        max_ = max(counter, max_)
        # TODO focus in edge case, this line of the string stretched to end, esp for block(1)

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
