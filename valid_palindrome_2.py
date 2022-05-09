# https://leetcode.com/problems/valid-palindrome-ii/

class Solution:
    def validPalindromeHelper_attempt_1(self, s: str, i: int, j: int):
        n = j - i + 1
        if n <= 1:
            return True
        cond1 = s[i] == s[j] and self.validPalindromeHelper(s, i + 1, j - 1)
        cond2 = s[i + 1] == s[j] and self.validPalindromeHelper(s, i + 2, j - 1)
        cond3 = s[i] == s[j - 1] and self.validPalindromeHelper(s, i + 1, j - 2)
        return cond1 or cond2 or cond3

    def validPalindrome_attempt_1(self, s: str) -> bool:
        return self.validPalindromeHelper(s, 0, len(s) - 1)

    def validPalindrome(self, s: str) -> bool:
        n = len(s)
        tolerance = 1
        if n <= 1:
            return True
        i = 0
        j = n - 1
        for direction in range(2):  # 0 skip a , 1 skip j
            while j >= i:
                if s[i] != s[j] and tolerance == 0:
                    return False
                elif s[i] != s[j] and tolerance == 1:
                    tolerance = 0
                    if direction == 0:
                        i = i + 1
                    else:
                        j = j - 1
                else:
                    i = i + 1
                    j = j - 1
        return True


if __name__ == '__main__':
    s = Solution()
    assert s.validPalindrome("abba") == True
    cases = [("aba", True), ("abca", True), ("abc", False)]
    for input, expected_output in cases:
        assert s.validPalindrome(input) == expected_output
    print(s.validPalindrome("aba"))
    print(s.validPalindrome("abba"))
    print(s.validPalindrome("a"))
    print(s.validPalindrome(""))
    print(s.validPalindrome("ab"))
    print(s.validPalindrome("abc"))
    print(s.validPalindrome("abca"))
