# https://leetcode.com/problems/valid-palindrome-ii/

class Solution:
    def validPalindromeHelper(self, s: str, i: int, j: int):
        n = j - i + 1
        if n <= 1:
            return True
        cond1 = s[i] == s[j] and self.validPalindromeHelper(s, i + 1, j - 1)
        cond2 = s[i + 1] == s[j] and self.validPalindromeHelper(s, i + 2, j - 1)
        cond3 = s[i] == s[j - 1] and self.validPalindromeHelper(s, i + 1, j - 2)
        return cond1 or cond2 or cond3

    def validPalindrome(self, s: str) -> bool:
        return self.validPalindromeHelper(s, 0, len(s) - 1)


if __name__ == '__main__':
    s = Solution()
    assert s.validPalindrome("abba") == True
    cases = [("aba", True), ("abca", True), ("abc", False)]
    for input, expected_output in cases:
        assert s.validPalindrome(input) == expected_output
